import os
import asyncio
from aiogram import Bot, Dispatcher

TOKEN = os.getenv("TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Например: https://yourapp.onrender.com/webhook

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    await bot.delete_webhook(drop_pending_updates=True)  # удаляем старый webhook
    await bot.set_webhook(WEBHOOK_URL)
    print(f"Webhook установлен: {WEBHOOK_URL}")
    await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
