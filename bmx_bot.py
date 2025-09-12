import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from fastapi import FastAPI, Request
from aiogram.types import Update

# Берем токен и ссылки из Environment Variables Render
TOKEN = os.getenv("TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
VIDEO_THREAD_ID = int(os.getenv("VIDEO_THREAD_ID"))
PHOTO_THREAD_ID = int(os.getenv("PHOTO_THREAD_ID"))

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher()
app = FastAPI()


# Команда /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Бот запущен! Я буду удалять сообщения, если они не подходят по типу.")


# Проверка сообщений в топиках
@dp.message()
async def check_messages(message: types.Message):
    thread_id = message.message_thread_id
    if thread_id == VIDEO_THREAD_ID and not message.video:
        await message.delete()
        return
    if thread_id == PHOTO_THREAD_ID and not message.photo:
        await message.delete()
        return


# Endpoint для webhook
@app.post(f"/webhook/{TOKEN}")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = Update(**data)
    await dp.update.process_update(update)
    return {"ok": True}


# Главная страница
@app.get("/")
async def root():
    return {"message": "Бот работает. Для установки webhook перейдите на /set_webhook"}


# Установка webhook при старте приложения
@app.on_event("startup")
async def on_startup():
    await bot.set_webhook(f"{WEBHOOK_URL}/webhook/{TOKEN}")
    print("Webhook установлен")
