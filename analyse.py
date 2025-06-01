import google.generativeai as genai
import re
from apiKey import key
from myprompts import ats_score_prompt, analysis_prompt

# Configure the API key
genai.configure(api_key=key)

# Create the generative model
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")

def clean_markdown_json(text):
    """Removes markdown-style code blocks like ```json ... ```"""
    return re.sub(r"```(?:json)?\s*([\s\S]*?)```", r"\1", text).strip()

def get_ats_score(resume_text, job_desc):
    prompt = f"{ats_score_prompt}\n\nResume:\n{resume_text}\n\nJob Description:\n{job_desc}"
    response = model.generate_content(prompt)
    return clean_markdown_json(response.text)

def get_resume_analysis(resume_text, software_used=None):
    software_info = f"\n\nNote: The resume was likely created using: {software_used}" if software_used else ""
    prompt = f"{analysis_prompt}\n\nResume:\n{resume_text}{software_info}"
    response = model.generate_content(prompt)
    return clean_markdown_json(response.text)
