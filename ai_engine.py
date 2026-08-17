import google.generativeai as genai
from app.config import AI_API_KEY
from app.logging_setup import logger

genai.configure(api_key=AI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def get_ai_response(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        logger.error(f"AI Error: {e}")
        return "দুঃখিত, এই মুহূর্তে AI কাজ করছে না।"
