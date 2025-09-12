# ========================РАБОТАЕТ ВРОДЕ НО НЕ ТАК===========================================
# import os
# from aiogram import Bot
# import asyncio

# TOKEN = os.getenv("TOKEN")
# WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# bot = Bot(token=TOKEN)

# async def main():
#     await bot.delete_webhook()
#     await bot.set_webhook(WEBHOOK_URL)
#     print(f"Webhook установлен: {WEBHOOK_URL}")

# if __name__ == "__main__":
#     asyncio.run(main())

# ========================РАБОТАЕТ ВРОДЕ НО НЕ ТАК===========================================
import os
import asyncio
from aiogram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
BASE_URL = os.getenv("BASE_URL")  # например, https://bmx-bot-hual.onrender.com

if not BOT_TOKEN or not BASE_URL:
    raise RuntimeError("BOT_TOKEN или BASE_URL не заданы!")

WEBHOOK_URL = f"{BASE_URL}/webhook/{BOT_TOKEN}"

async def main():
    bot = Bot(token=BOT_TOKEN)
    await bot.delete_webhook()
    await bot.set_webhook(WEBHOOK_URL)
    await bot.session.close()

asyncio.run(main())
