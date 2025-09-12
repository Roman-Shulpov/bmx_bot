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
WEBHOOK_URL = f"https://bmx-bot-hual.onrender.com/webhook/{BOT_TOKEN}"

async def main():
    bot = Bot(token=BOT_TOKEN)
    await bot.set_webhook(WEBHOOK_URL)
    print(f"Webhook установлен на {WEBHOOK_URL}")

if __name__ == "__main__":
    asyncio.run(main())
