# app/admin_bot.py
from aiogram import Router, types
from aiogram.filters import Command

admin_router = Router()

@admin_router.message(Command("admin"))
async def admin_panel(message: types.Message):
    await message.answer("Welcome to the Admin Panel.")
