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
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from fastapi import FastAPI, Request
from aiogram.types import Update
from handlers import video_photo  # твой обработчик сообщений

logging.basicConfig(level=logging.INFO)

# Получение токена из Environment Variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN не задан! Проверь переменные окружения.")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Подключаем хэндлеры
video_photo.register_handlers(dp)

app = FastAPI()

WEBHOOK_PATH = f"/webhook/{BOT_TOKEN}"
WEBHOOK_URL = f"https://{os.getenv('RENDER_EXTERNAL_HOSTNAME')}{WEBHOOK_PATH}"

# Endpoint для Telegram webhook
@app.post(WEBHOOK_PATH)
async def telegram_webhook(request: Request):
    update = Update(**await request.json())
    await dp.process_update(update)
    return {"ok": True}

# Для проверки, что сервер жив
@app.get("/")
async def root():
    return {"status": "Bot is running!"}

# Если хочешь запускать через uvicorn локально:
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("bmx_bot:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)))


