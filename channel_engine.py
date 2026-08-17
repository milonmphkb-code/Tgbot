from app.logging_setup import logger

async def post_to_channel(context, channel_id: str, text: str):
    try:
        await context.bot.send_message(chat_id=channel_id, text=text)
        logger.info("Successfully posted to channel.")
    except Exception as e:
        logger.error(f"Failed to post to channel: {e}")
