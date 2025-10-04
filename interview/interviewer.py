# interview/interviewer.py
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime
import uuid
import os
import json
from langchain_groq import ChatGroq



MAX_FOLLOWUPS_PER_QUESTION = 2

@dataclass
class Agent:
    """
    Agent decides next action given question, expected answer, and candidate answer.
    Uses LLM if API key present; otherwise uses deterministic heuristics.
    Actions: 'followup', 'hint', 'accept', 'clarify', 'next'
    Response: {'action':..., 'message': ...}
    """
    llm_api_key: Optional[str] = None
    provider: str = "groq"

    def plan_action(self, question_text: str, expected: str, candidate_answer: str, used_hint: bool):
        # If LLM key present, ask it to decide
        if self.llm_api_key :
            try:
                prompt = (
                    "You are an interview agent for Excel skills. Given the question, the expected answer/hints, and the candidate's answer, "
                    "choose a single action from: followup, hint, accept, clarify, next. "
                    "Also provide a short 'message' (follow-up question or hint). Respond ONLY in JSON: {\"action\":\"...\",\"message\":\"...\"}.\n\n"
                    f"Question: {question_text}\nExpected: {expected}\nCandidate answer: {candidate_answer}\nUsed_hint: {used_hint}\n\nBe concise."
                )
                
                messages=[
                        {"role": "system", "content": "You are an objective, concise interviewer agent."},
                        {"role": "user", "content": prompt}
                    ]

                llm = ChatGroq(
                    model="openai/gpt-oss-120b",
                    temperature=0,
                    max_tokens=None,
                    reasoning_format="parsed",
                    timeout=None,
                    max_retries=2,
                    # other params...
                )
                resp = llm.invoke(messages)
                text = resp.content.strip()
                # Attempt to parse JSON
                data = json.loads(text)
                action = data.get("action", "followup")
                message = data.get("message", "")
                return {"action": action, "message": message}
            except Exception as e:
                # fallback to heuristics
                # print("Agent LLM error:", e)
                pass

        # Heuristic fallback
        ca = (candidate_answer or "").lower()
        exp = (expected or "").lower()
        # if no answer -> ask clarify
        if not ca.strip():
            return {"action": "clarify", "message": "Could you walk me through how you'd approach this (step-by-step)?"}
        # if candidate uses expected tokens -> accept
        match_tokens = sum(1 for t in ["sumif", "sumifs", "text(", "vlookup", "xlookup", "index(", "match(", "large(", "power query", "pivot"] if t in ca or t in exp)
        if match_tokens >= 1:
            # if they asked for hint earlier and used it, still accept
            return {"action": "accept", "message": "Thanks — that looks reasonable. I may ask one quick follow-up."}
        # if candidate expresses uncertainty
        if any(p in ca for p in ["not sure", "i don't know", "dont know", "unsure"]):
            return {"action": "hint", "message": "Think about normalizing IDs (TRIM/VALUE/TEXT) or using Power Query merge — would that help?"}
        # otherwise ask a targeted follow-up to understand reasoning
        return {"action": "followup", "message": "Can you explain why you chose that approach and any edge-cases you'd consider?"}


@dataclass
class InterviewManager:
    role: str
    questions: List[Dict]
    session_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    start_ts: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    current_index: int = 0
    answered: List[Dict] = field(default_factory=list)
    agent: Agent = field(default_factory=lambda: Agent(llm_api_key=os.getenv("LLM_API_KEY", ""), provider=os.getenv("LLM_PROVIDER", "groq")))
    # pending agent message waiting for candidate reply
    pending_agent_message: Optional[str] = None
    # track followup counts per question index
    followup_counts: Dict[int, int] = field(default_factory=dict)

    def current_question(self) -> Optional[Dict]:
        if self.current_index < len(self.questions):
            return self.questions[self.current_index]
        return None

    def submit_initial_answer(self, answer_text: str, used_hint: bool=False, llm_api_key: Optional[str]=""):
        """
        Called when candidate submits first answer for current question.
        Agent will plan next action (followup/hint/accept).
        """
        q = self.current_question()
        if q is None:
            return
        entry = {
            "question_id": q["id"],
            "question_text": q["prompt"],
            "answer_text": answer_text,
            "expected": q.get("expected", ""),
            "type": q.get("type", ""),
            "used_hint": used_hint,
            "followups": [],
            "timestamp": datetime.utcnow().isoformat()
        }
        self.answered.append(entry)
        # plan action
        plan = self.agent.plan_action(q["prompt"], q.get("expected", ""), answer_text, used_hint)
        # if followup/hint/clarify -> set pending_agent_message
        if plan["action"] in ("followup", "hint", "clarify"):
            self.pending_agent_message = plan["message"] or "Please clarify your approach."
            # initialize followup count
            self.followup_counts[self.current_index] = 0
        else:
            self.pending_agent_message = None
            self.current_index += 1

    def process_followup_reply(self, reply_text: str, llm_api_key: Optional[str]=""):
        """
        Called when candidate replies to an agent followup. Agent decides whether to continue followups or accept.
        """
        if not self.answered:
            return
        last_entry = self.answered[-1]
        # append followup reply
        last_entry["followups"].append({"text": reply_text, "timestamp": datetime.utcnow().isoformat()})
        # increment followup count
        count = self.followup_counts.get(self.current_index, 0) + 1
        self.followup_counts[self.current_index] = count
        # agent decides based on this reply
        q = self.current_question()
        plan = self.agent.plan_action(q["prompt"], q.get("expected", ""), reply_text, last_entry.get("used_hint", False))
        if plan["action"] in ("followup", "clarify", "hint") and count < MAX_FOLLOWUPS_PER_QUESTION:
            # agent wants further follow-up
            self.pending_agent_message = plan["message"] or "Please elaborate further."
        else:
            # accept and move to next
            self.pending_agent_message = None
            self.current_index += 1

    def process_answer(self, answer_text: str, used_hint: bool=False, llm_api_key: Optional[str]=""):
        """
        New unified entry point used by app: it will call submit_initial_answer or if pending agent message exists, defer to process_followup_reply.
        """
        if self.pending_agent_message:
            # treat this as follow-up reply
            self.process_followup_reply(answer_text, llm_api_key=llm_api_key)
        else:
            self.submit_initial_answer(answer_text, used_hint=used_hint, llm_api_key=llm_api_key)

    def finalize_current_question(self):
        """Force finalize current question (used when skipping a followup)."""
        self.pending_agent_message = None
        self.current_index += 1

    def is_complete(self) -> bool:
        return self.current_index >= len(self.questions)
