# ========================РАБОТАЕТ ВРОДЕ НО НЕ ТАК===========================================

# import os
# from fastapi import FastAPI, Request
# from aiogram import Bot, Dispatcher, types
# from aiogram.types import Update
# from handlers import video_photo

# TOKEN = os.getenv("TOKEN")
# bot = Bot(token=TOKEN, parse_mode="HTML")
# dp = Dispatcher()
# video_photo.register_handlers(dp)

# app = FastAPI()

# @app.post("/webhook")
# async def telegram_webhook(req: Request):
#     data = await req.json()
#     update = Update(**data)
#     await dp.update_router.dispatch(update)
#     return {"ok": True}

# ========================РАБОТАЕТ ВРОДЕ НО НЕ ТАК===========================================
import os
from aiogram import Bot, Dispatcher, types
from fastapi import FastAPI, Request
from aiogram.types import Update
from aiogram.dispatcher.webhook import get_new_configured_app
from handlers.video_photo import check_and_delete_message

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN не задан! Проверь переменные окружения.")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

app = FastAPI()

# --- Обработчик любых сообщений ---
@dp.message()
async def handle_message(message: types.Message):
    await check_and_delete_message(bot, message)

# --- Webhook endpoint ---
@app.post("/webhook/{token}")
async def webhook_handler(token: str, request: Request):
    if token != BOT_TOKEN:
        return {"status": "unauthorized"}

    data = await request.json()
    update = Update(**data)
    await dp.update_queue.put(update)
    return {"status": "ok"}

# --- Для локального теста ---
@app.get("/")
async def index():
    return {"status": "Bot is running"}


