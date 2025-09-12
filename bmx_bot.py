import os
from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types
from aiogram.types import Update
from handlers import video_photo

TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher()
video_photo.register_handlers(dp)

app = FastAPI()

@app.post("/webhook")
async def telegram_webhook(req: Request):
    data = await req.json()
    update = Update(**data)
    await dp.update_router.dispatch(update)
    return {"ok": True}
