import google.generativeai as genai
from apiKey import key

# Configure Gemini API
genai.configure(api_key=key)

# Initialize the Gemini model (latest flash version)
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")

# Prompt for enhanced CV generation tailored for ATS and Naukri.com style
generate_prompt = """
You're a professional resume writer. Based on the input resume and job description, generate an improved resume content tailored for the role. 
Use concise bullet points, professional formatting, and optimize it to score highly on ATS systems.
Format the resume to follow the style and layout similar to Naukri.com resume templates.
Provide at least 100 points of improvement or optimization to ensure maximum ATS score and recruiter impact.
"""

def generate_enhanced_cv(resume_text, job_desc):
    full_prompt = f"{generate_prompt}\n\nResume:\n{resume_text}\n\nJob Description:\n{job_desc}"
    response = model.generate_content(full_prompt)
    return response.text
