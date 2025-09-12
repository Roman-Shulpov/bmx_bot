import os
import asyncio
from fastapi import FastAPI
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Filter
from aiogram.dispatcher.webhook import get_new_configured_app

# Переменные окружения
TOKEN = os.getenv("TOKEN")
VIDEO_THREAD_ID = int(os.getenv("VIDEO_THREAD_ID"))
PHOTO_THREAD_ID = int(os.getenv("PHOTO_THREAD_ID"))

# Создаем бота и диспетчер
bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher()

# Фильтры для проверки сообщений
class NoVideoFilter(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.chat.id == VIDEO_THREAD_ID and not message.video

class NoPhotoFilter(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.chat.id == PHOTO_THREAD_ID and not message.photo

# Хэндлеры для удаления ненужных сообщений
@dp.message(NoVideoFilter())
async def delete_no_video(message: Message):
    try:
        await message.delete()
    except Exception as e:
        print(f"Error deleting message without video: {e}")

@dp.message(NoPhotoFilter())
async def delete_no_photo(message: Message):
    try:
        await message.delete()
    except Exception as e:
        print(f"Error deleting message without photo: {e}")

# Создаем FastAPI app, который Render сможет увидеть
app: FastAPI = get_new_configured_app(dispatcher=dp, path="/webhook")

# Для локального запуска polling (не для Render)
if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
