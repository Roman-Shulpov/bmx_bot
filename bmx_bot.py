import os
import asyncio
from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Filter
from aiogram.dispatcher.event.handler import CancelHandler

TOKEN = os.getenv("TOKEN")
VIDEO_THREAD_ID = int(os.getenv("VIDEO_THREAD_ID"))
PHOTO_THREAD_ID = int(os.getenv("PHOTO_THREAD_ID"))

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher()

# Фильтры
class NoVideoFilter(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.chat.id == VIDEO_THREAD_ID and not message.video

class NoPhotoFilter(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.chat.id == PHOTO_THREAD_ID and not message.photo

# Хэндлеры
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

# FastAPI app
app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    update = types.Update(**data)
    await dp.feed_update(update)
    return {"ok": True}

# Для локального запуска polling
if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
