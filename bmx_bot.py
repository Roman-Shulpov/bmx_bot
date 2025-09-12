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
from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types
from aiogram.types import Update
from aiogram.utils.exceptions import TelegramAPIError
from handlers.video_photo import check_message

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN не задан! Проверь переменные окружения.")

WEBHOOK_PATH = f"/webhook/{BOT_TOKEN}"
WEBHOOK_URL = f"{os.getenv('BASE_URL')}{WEBHOOK_PATH}"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
app = FastAPI()

# Корневой эндпоинт для проверки
@app.get("/")
async def root():
    return {"status": "Bot is running!"}

# Webhook endpoint
@app.post(WEBHOOK_PATH)
async def telegram_webhook(update: Request):
    data = await update.json()
    update_obj = Update(**data)
    try:
        await check_message(bot, update_obj)
    except TelegramAPIError:
        pass
    return {"ok": True}

# Запуск вебхука через set_webhook.py
