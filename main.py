from telegram.ext import Application, CommandHandler, MessageHandler, filters
from app.config import load_settings
from app.logging_setup import logger
from app.admin_bot import admin_start
from app.group_bot import handle_group_message

def main():
    logger.info("Starting the bot...")
    
    # লোড সেটিংস
    BOT_TOKEN, AI_API_KEY, DATABASE_URL = load_settings()
    
    # অ্যাপলিকেশন তৈরি
    application = Application.builder().token(BOT_TOKEN).build()
    
    # হ্যান্ডলার যুক্ত করা
    application.add_handler(CommandHandler("admin", admin_start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_group_message))
    
    # বট রান করা
    logger.info("Bot is polling...")
    application.run_polling()

if __name__ == "__main__":
    main()
