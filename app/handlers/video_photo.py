from aiogram import Router, F
from aiogram.types import Message
import logging
from app.config import ALLOWED_CHAT_IDS

router = Router()
logger = logging.getLogger(__name__)


@router.message(F.chat.id.in_(ALLOWED_CHAT_IDS))
async def handle_media(message: Message):
    logger.info(
        f"New message in allowed chat: {message.chat.id}, photo: {bool(message.photo)}, video: {bool(message.video)}")

    if message.photo or message.video:
        return

    try:
        await message.delete()
        logger.info("Message deleted ✅")
    except Exception as e:
        logger.error(f"Failed to delete message: {e}")
