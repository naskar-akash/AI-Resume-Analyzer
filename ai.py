from openai import OpenAI
from dotenv import load_dotenv
import json 
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def analyse_resume(resume_text, user_goal):

    prompt = f"""
        You are a senior software engineer and hiring manager.
        Evaluate the resume based on the user's goal.
        User goal: "{user_goal}"

        STRICT RULES:
        ~ Extract only relevent skills for this goal
        ~ Remove irrelevent tools [excel for backend etc.]
        ~ Identify real gaps
        ~ Generate roadmap only for missing fields
        ~ Make output different based on goal

        Return only JSON:
        {{
        "skills": [],
        "missing_skills": [],
        "roadmap": [],
        "interview_questions": []
        }}
        Resume: {resume_text}
            """
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are a strict hiring manager"},
                {"role": "user", "content": prompt}
            ]
        )
        content = response.choices[0].message.content.strip()