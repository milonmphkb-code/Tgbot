# app/group_bot.py
from aiogram import Router, types

group_router = Router()

@group_router.message()
async def handle_group_messages(message: types.Message):
    # Placeholder for group chat message handling
    pass
