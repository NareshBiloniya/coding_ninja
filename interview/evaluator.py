
import os
import json
from typing import Dict
from datetime import datetime
from langchain_groq import ChatGroq


# Rubric weights
RUBRIC_WEIGHTS = {
    "formula_accuracy": 0.30,
    "logical_thinking": 0.25,
    "learning_willingness": 0.10,
    "complex_scenario": 0.20,
    "communication": 0.15
}
PASS_THRESHOLD = 7.0

def safe_round(x):
    return round(max(0, min(10, x)), 1)

def evaluate_with_openai(prompt: str, api_key: str):
    if not api_key:
        return None
    try:        
        messages=[
                {"role": "system", "content": "You are an objective Excel evaluator. Return JSON only."},
                {"role": "user", "content": prompt}
            ]

        llm = ChatGroq(
            model="openai/gpt-oss-120b",
            temperature=0,
            max_tokens=500,
            reasoning_format="parsed",
            timeout=None,
            max_retries=2,
            # other params...
        )
        resp = llm.invoke(messages)
        text = resp.content.strip()
        return json.loads(text)
    except Exception as e:
        # print("LLM eval error:", e)
        return None

def fallback_eval_text(question_text: str, expected: str, candidate_text: str, used_hint: bool):
    ca = (candidate_text or "").lower()
    exp = (expected or "").lower()
    scores = {}
    # formula_accuracy
    fa = 0
    for tok in ["sumif", "sumifs", "text(", "large(", "index(", "match(", "xlookup", "vlookup", "pivot", "power query", "sql"]:
        if tok in ca or tok in exp:
            fa += 2
    fa = min(10, fa)
    scores["formula_accuracy"] = safe_round(fa)
    # logical_thinking
    lt = 6 if any(w in ca for w in ["because", "first", "then", "next", "normalize", "merge", "step", "approach"]) else 5
    scores["logical_thinking"] = safe_round(lt)
    # learning_willingness
    lw = 8 if used_hint or any(w in ca for w in ["learn", "curious", "try"]) else 6
    scores["learning_willingness"] = safe_round(lw)
    # complex_scenario
    cs = 7 if any(w in ca for w in ["power query", "sql", "helper", "aggregate", "pivot"]) else 5
    scores["complex_scenario"] = safe_round(cs)
    # communication
    comm = min(10, max(3, round(len(ca.split()) / 4)))
    scores["communication"] = safe_round(comm)

    return {
        "category_scores": scores,
        "justification": "Fallback evaluator used.",
        "resources": ["Microsoft Docs - Excel functions", "Power Query tutorials"]
    }

def evaluate_session(interview_mgr, llm_api_key: str=""):
    """
    Evaluate each answered question (including followups concatenated) and return aggregated evaluation.
    """
    details = []
    agg = {k: 0.0 for k in RUBRIC_WEIGHTS.keys()}
    n = max(1, len(interview_mgr.answered))
    for entry in interview_mgr.answered:
        qtext = entry.get("question_text", "")
        expected = entry.get("expected", "")
        # combine main answer + followups for evaluation context
        combined_answer = entry.get("answer_text", "")
        if entry.get("followups"):
            combined_answer += " " + " ".join(fu.get("text","") for fu in entry.get("followups", []))
        used_hint = bool(entry.get("used_hint", False))
        eval_json = None
        if llm_api_key:
            prompt = (
                "Evaluate this candidate answer for the Excel interview and return JSON with fields: "
                "{\"category_scores\": {\"formula_accuracy\":float, \"logical_thinking\":float, "
                "\"learning_willingness\":float, \"complex_scenario\":float, \"communication\":float}, "
                "\"justification\": \"...\", \"resources\": [..]}\n"
                f"Question: {qtext}\nExpected: {expected}\nCandidate combined answer: {combined_answer}\nUsed hint: {used_hint}"
            )
            eval_json = evaluate_with_openai(prompt, llm_api_key)
        if eval_json is None:
            eval_json = fallback_eval_text(qtext, expected, combined_answer, used_hint)
        cat_scores = eval_json.get("category_scores", {})
        for k in RUBRIC_WEIGHTS.keys():
            agg[k] += cat_scores.get(k, 0)
        details.append({
            "question_text": qtext,
            "answer_text": combined_answer,
            "eval_json": eval_json
        })
    # average & compute combined
    avg = {k: round(agg[k] / n, 1) for k in agg.keys()}
    combined = 0.0
    for k, w in RUBRIC_WEIGHTS.items():
        combined += avg.get(k, 0) * w
    combined = round(combined, 1)
    pass_bool = combined >= PASS_THRESHOLD
    return {
        "avg_category_scores": avg,
        "combined_score": combined,
        "pass_bool": pass_bool,
        "details": details,
        "session_id": interview_mgr.session_id,
        "evaluated_at": datetime.utcnow().isoformat()
    }
