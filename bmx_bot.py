import os
import logging
from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentType
from aiogram.dispatcher.webhook import get_new_configured_app

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
VIDEO_THREAD_ID = int(os.getenv("VIDEO_THREAD_ID"))  # топик для видео
PHOTO_THREAD_ID = int(os.getenv("PHOTO_THREAD_ID"))  # топик для фото

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    logging.info("Приложение стартовало. Webhook НЕ установлен автоматически.")

@app.get("/")
async def root():
    return {"message": "Бот запущен. Для установки webhook перейдите на /set_webhook"}

@app.get("/set_webhook")
async def set_webhook():
    await bot.set_webhook(f"{WEBHOOK_URL}/webhook/{TOKEN}")
    return {"message": "Webhook установлен!"}

@app.post("/webhook/{token}")
async def telegram_webhook(token: str, request: Request):
    if token != TOKEN:
        return {"status": "invalid token"}
    update = types.Update(**await request.json())
    await dp.process_update(update)
    return {"status": "ok"}

# Обработчик сообщений
@dp.message_handler()
async def delete_wrong_messages(message: types.Message):
    if message.is_topic_message:
        thread_id = message.message_thread_id
        if thread_id == VIDEO_THREAD_ID:
            if not message.video:
                await message.delete()
        elif thread_id == PHOTO_THREAD_ID:
            if not message.photo:
                await message.delete()
