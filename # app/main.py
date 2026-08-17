# app/main.py
import asyncio
import logging
from app.config import BOT_TOKEN
from aiogram import Bot, Dispatcher

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def main():
    logging.info("Bot is starting...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
