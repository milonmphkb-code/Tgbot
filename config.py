import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
AI_API_KEY = os.getenv("AI_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")

def load_settings():
    if not BOT_TOKEN or not AI_API_KEY:
        raise ValueError("BOT_TOKEN or AI_API_KEY is missing in environment variables!")
    return BOT_TOKEN, AI_API_KEY, DATABASE_URL
