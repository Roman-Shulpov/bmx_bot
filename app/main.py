import logging
from fastapi import FastAPI
from aiogram import Bot, Dispatcher
from aiogram.types import Update

from app.handlers import video_photo
from app.config import BOT_TOKEN, WEBHOOK_URL

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(video_photo.router)

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await bot.set_webhook(f"{WEBHOOK_URL}/webhook")
    logger.info(f"✅ Webhook установлен: {WEBHOOK_URL}/webhook")


@app.get("/")
async def root():
    return {"status": "ok", "message": "Bot is running 🚀"}


@app.post("/webhook")
async def telegram_webhook(update: dict):
    telegram_update = Update(**update)
    await dp.feed_update(bot, telegram_update)
    return {"ok": True}
