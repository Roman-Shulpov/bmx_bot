import os
import asyncio
from aiogram import Bot

TOKEN = os.getenv("TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

async def main():
    bot = Bot(token=TOKEN)
    await bot.set_webhook(f"{WEBHOOK_URL}/webhook/{TOKEN}")
    print("Webhook установлен вручную")

asyncio.run(main())
