import os
import asyncio
from aiogram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Должно быть HTTPS

async def set_webhook():
    bot = Bot(token=BOT_TOKEN)
    await bot.set_webhook(f"{WEBHOOK_URL}/webhook")
    print(f"Webhook установлен: {WEBHOOK_URL}/webhook")
    await bot.session.close()

if __name__ == "__main__":
    asyncio.run(set_webhook())
