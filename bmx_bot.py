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
from fastapi import FastAPI
from aiogram import Bot, Dispatcher
from aiogram.types import Update

from handlers import video_photo

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(video_photo.router)

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await bot.set_webhook(WEBHOOK_URL)


@app.post("/")
async def telegram_webhook(update: dict):
    telegram_update = Update(**update)
    await dp.feed_update(bot, telegram_update)
    return {"ok": True}

