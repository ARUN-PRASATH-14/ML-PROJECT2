import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


model = genai.GenerativeModel("models/gemini-2.5-flash-lite")

def analyze_career(profile_text):
    prompt = f"""
    You are an expert AI career counselor in the year 2026.

    Analyze the following student profile and:
    1. Recommend the TOP 3 career roles (relevant in 2026)
    2. Give a short reason for each role
    3. Provide a clear step-by-step learning roadmap

    Student Profile:
    {profile_text}

    Keep the response structured and practical.
    """

    response = model.generate_content(prompt)
    return response.text
