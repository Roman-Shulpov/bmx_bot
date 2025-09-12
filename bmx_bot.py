# bmx_bot.py
import logging
import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = "7976564635:AAGr4yMj4jDk5Lu6wam9JOfvkSrwHw0eYzg"
BOT_CHAT_ID = -1002097447
VIDEO_THREAD_ID = 4
PHOTO_THREAD_ID = 12

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- Проверка содержимого сообщений ---
def message_contains_image(msg: types.Message) -> bool:
    if msg.photo:
        return True
    if msg.document and msg.document.mime_type and msg.document.mime_type.startswith("image/"):
        return True
    return False

def message_contains_video(msg: types.Message) -> bool:
    if msg.video or msg.video_note or msg.animation:
        return True
    if msg.document and msg.document.mime_type and msg.document.mime_type.startswith("video/"):
        return True
    return False

# --- Фильтрация сообщений ---
@dp.message()
async def filter_by_thread(message: types.Message):
    thread_id = message.message_thread_id
    if thread_id is None:
        return
    try:
        if thread_id == VIDEO_THREAD_ID and not message_contains_video(message):
            await message.delete()
        elif thread_id == PHOTO_THREAD_ID and not message_contains_image(message):
            await message.delete()
    except Exception as e:
        logger.exception("Ошибка при обработке сообщения: %s", e)

# --- Эхо-хендлер для текста ---
@dp.message()
async def echo(message: types.Message):
    if message.text:
        await message.answer(message.text)

# --- Запуск long-polling ---
async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
