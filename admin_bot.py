from telegram import Update
from telegram.ext import ContextTypes
from app.logging_setup import logger

async def admin_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("Admin command triggered")
    await update.message.reply_text("হ্যালো অ্যাডমিন! আমি প্রস্তুত।")
