
import io
import csv
import json

def compile_report(interview_mgr, eval_result):
    report = {
        "session_id": interview_mgr.session_id,
        "role": interview_mgr.role,
        "start_ts": interview_mgr.start_ts,
        "end_ts": eval_result.get("evaluated_at"),
        "avg_category_scores": eval_result.get("avg_category_scores"),
        "combined_score": eval_result.get("combined_score"),
        "pass_bool": eval_result.get("pass_bool"),
        "details": eval_result.get("details")
    }
    return report

def export_report_csv(report_dict):
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["question_text", "answer_text", "eval_json"])
    for d in report_dict.get("details", []):
        writer.writerow([d.get("question_text", ""), d.get("answer_text", ""), json.dumps(d.get("eval_json", {}))])
    return output.getvalue().encode("utf-8")
