import asyncio
from aiogram import Bot

TOKEN = "7976564635:AAGr4yMj4jDk5Lu6wam9JOfvkSrwHw0eYzg"
WEBHOOK_URL = f"https://bmx-bot-hual.onrender.com/webhook/{TOKEN}"

async def main():
    bot = Bot(token=TOKEN)
    await bot.set_webhook(WEBHOOK_URL)
    print(f"Webhook установлен: {WEBHOOK_URL}")
    await bot.session.close()

asyncio.run(main())
