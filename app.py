

import os
import streamlit as st
from dotenv import load_dotenv
from interview.questions import get_questions_for_role
from interview.interviewer import InterviewManager
from interview.evaluator import evaluate_session
from interview.report import compile_report, export_report_csv
import pandas as pd

# Load .env
load_dotenv()
LLM_API_KEY = os.getenv("LLM_API_KEY", "")

st.set_page_config(page_title="Excel Mock Interviewer - PoC", layout="wide")
st.title("Excel Mock Interviewer — PoC")

# Simple sign-in stored in session_state (no DB)
if "user" not in st.session_state:
    st.session_state.user = None

with st.sidebar:
    st.header("Sign in")
    if st.session_state.user is None:
        email = st.text_input("Email (demo only)")
        if st.button("Sign in / create"):
            if not email:
                st.error("Enter an email to sign in.")
            else:
                st.session_state.user = {"email": email}
                st.success(f"Signed in as {email}")
                st.experimental_rerun = st.experimental_rerun if hasattr(st, "experimental_rerun") else lambda: st.stop()
                st.experimental_rerun()

    else:
        st.markdown(f"**Signed in as:** {st.session_state.user['email']}")
        if st.button("Sign out"):
            st.session_state.user = None
            st.experimental_rerun = st.experimental_rerun if hasattr(st, "experimental_rerun") else lambda: st.stop()
            st.experimental_rerun()


if st.session_state.user is None:
    st.info("Please sign in from the sidebar to start the interview.")
    st.stop()

# Pages
page = st.sidebar.selectbox("Page", ["Dashboard", "Start Interview", "Reports"])

# Initialize interview manager in session
if "interview_mgr" not in st.session_state:
    st.session_state.interview_mgr = None

if page == "Dashboard":
    st.header("Dashboard")
    st.markdown("Start a new interview or resume current one.")
    if st.button("Start new interview"):
        st.session_state.interview_mgr = None
        st.experimental_rerun = st.experimental_rerun if hasattr(st, "experimental_rerun") else lambda: st.stop()
        st.experimental_rerun()


    if st.session_state.interview_mgr is None:
        st.info("No active session. Go to 'Start Interview' to begin.")
    else:
        mgr: InterviewManager = st.session_state.interview_mgr
        st.write("Active session for role:", mgr.role)
        st.write("Questions answered:", len(mgr.answered))
        if st.button("Resume interview"):
            page = "Start Interview"
            st.experimental_rerun = st.experimental_rerun if hasattr(st, "experimental_rerun") else lambda: st.stop()
            st.experimental_rerun()


elif page == "Start Interview":
    st.header("Start Interview")
    if st.session_state.interview_mgr is None:
        role = st.selectbox("Select role level", ["associate", "above_associate", "senior"])
        if st.button("Begin Interview"):
            questions = get_questions_for_role(role)
            st.session_state.interview_mgr = InterviewManager(role=role, questions=questions)
            st.experimental_rerun = st.experimental_rerun if hasattr(st, "experimental_rerun") else lambda: st.stop()
            st.experimental_rerun()

    else:
        mgr: InterviewManager = st.session_state.interview_mgr
        st.markdown(f"**Interviewer (friendly)** — Role: {mgr.role}")
        if mgr.is_complete():
            st.success("Interview complete. Click Evaluate to grade.")
            if st.button("Evaluate"):
                # Evaluate using LLM if available; otherwise fallback
                eval_result = evaluate_session(mgr, llm_api_key=LLM_API_KEY)
                report = compile_report(mgr, eval_result)
                st.session_state.last_report = report
                st.experimental_rerun = st.experimental_rerun if hasattr(st, "experimental_rerun") else lambda: st.stop()
                st.experimental_rerun()

        else:
            q = mgr.current_question()
            st.markdown(f"### Q{mgr.current_index + 1}: {q['prompt']}")
            ans = st.text_area("Your answer (type formula or explanation)", value="", height=150)
            hint = st.checkbox("Request a hint (counts toward learning willingness)")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Submit Answer"):
                    if not ans.strip():
                        st.error("Please enter an answer before submitting.")
                    else:
                        mgr.process_answer(ans.strip(), used_hint=hint)
                        st.session_state.interview_mgr = mgr
                        st.experimental_rerun = st.experimental_rerun if hasattr(st, "experimental_rerun") else lambda: st.stop()
                        st.experimental_rerun()

            with col2:
                if st.button("Skip Question"):
                    mgr.process_answer("", used_hint=hint)
                    st.session_state.interview_mgr = mgr
                    st.experimental_rerun = st.experimental_rerun if hasattr(st, "experimental_rerun") else lambda: st.stop()
                    st.experimental_rerun()


elif page == "Reports":
    st.header("Reports")
    report = st.session_state.get("last_report", None)
    if report is None:
        st.info("No report available. Complete an interview and click Evaluate.")
    else:
        st.subheader("Summary")
        st.write("Combined score:", report["combined_score"])
        st.write("Pass:", "Yes" if report["pass_bool"] else "No")
        st.subheader("Category Scores")
        st.table(pd.DataFrame(report["avg_category_scores"], index=[0]).T.rename(columns={0: "score"}))
        st.subheader("Details")
        for item in report["details"]:
            st.markdown(f"**Q:** {item['question_text']}")
            st.markdown(f"**Answer:** {item['answer_text']}")
            st.markdown(f"**Eval:** {item['eval_json']}")
        csv_bytes = export_report_csv(report)
        st.download_button("Download report CSV", csv_bytes, file_name=f"report_{report['session_id']}.csv")
