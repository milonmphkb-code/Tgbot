# app/ai_engine.py
import google.generativeai as genai
from app.config import AI_API_KEY

genai.configure(api_key=AI_API_KEY)

def generate_ai_response(prompt: str) -> str:
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating AI response: {str(e)}"
