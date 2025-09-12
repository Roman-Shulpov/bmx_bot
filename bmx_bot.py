import os
import logging
from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentType

logging.basicConfig(level=logging.INFO)

# Берём токен и URL webhook из Environment Variables
TOKEN = os.getenv("TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# ID топиков (thread_id) для видео и фото
VIDEO_THREAD_ID = int(os.getenv("VIDEO_THREAD_ID"))  # топик для видео
PHOTO_THREAD_ID = int(os.getenv("PHOTO_THREAD_ID"))  # топик для фото

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

app = FastAPI()

# --- Хэндлер удаления сообщений ---
@dp.message_handler()
async def check_message(message: types.Message):
    try:
        # Удаляем в видео-топике, если нет видео
        if message.chat.id == VIDEO_THREAD_ID:
            if not message.video:
                await message.delete()
                logging.info(f"Удалено сообщение {message.message_id} без видео")
        # Удаляем в фото-топике, если нет фото
        elif message.chat.id == PHOTO_THREAD_ID:
            if not message.photo:
                await message.delete()
                logging.info(f"Удалено сообщение {message.message_id} без фото")
    except Exception as e:
        logging.error(f"Ошибка при удалении сообщения: {e}")

# --- FastAPI endpoint для webhook ---
@app.post(f"/webhook/{TOKEN}")
async def telegram_webhook(request: Request):
    update = types.Update(**await request.json())
    await dp.process_update(update)
    return {"ok": True}

@app.get("/")
async def root():
    return {"message": "Бот запущен. Чтобы установить webhook, перейдите на /set_webhook"}

# --- Установка webhook (один раз) ---
@app.get("/set_webhook")
async def set_webhook():
    webhook_url = f"{WEBHOOK_URL}/webhook/{TOKEN}"
    await bot.set_webhook(webhook_url)
    return {"message": f"Webhook установлен: {webhook_url}"}
