import streamlit as st
from fileloader import load_resume
from analyse import get_ats_score, get_resume_analysis
from generate import generate_enhanced_cv
import tempfile

st.set_page_config(page_title="Resume Analyzer", layout="wide")

st.title("📄 AI Resume Analyzer & Enhancer")

# Upload section
uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])
job_desc = st.text_area("Paste the Job Description here")

if uploaded_file and job_desc:
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        resume_text = load_resume(temp_file.name)

    # Tabs for different sections
    tab1, tab2, tab3 = st.tabs(["✅ ATS Score", "🧠 Resume Analysis", "🪄 Generate Enhanced CV"])

    with tab1:
        st.subheader("📊 ATS Score")
        ats_score = get_ats_score(resume_text, job_desc)
        st.json(ats_score)

    with tab2:
        st.subheader("🧠 Detailed Analysis")
        analysis = get_resume_analysis(resume_text)
        st.json(analysis)

    with tab3:
        st.subheader("🪄 Enhanced CV")
        enhanced_cv = generate_enhanced_cv(resume_text, job_desc)
        st.text_area("Enhanced Resume", value=enhanced_cv, height=600)
