from telegram import Update
from telegram.ext import ContextTypes
from app.ai_engine import get_ai_response
from app.logging_setup import logger

async def handle_group_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    logger.info(f"Received group message: {user_message}")
    
    ai_reply = get_ai_response(user_message)
    await update.message.reply_text(ai_reply)
