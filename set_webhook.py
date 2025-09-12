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
from aiogram import Bot
import asyncio

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Пример: https://bmx-bot-hual.onrender.com/webhook/{BOT_TOKEN}

if not BOT_TOKEN or not WEBHOOK_URL:
    raise RuntimeError("BOT_TOKEN или WEBHOOK_URL не задан!")

bot = Bot(token=BOT_TOKEN)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(WEBHOOK_URL)
    print("Webhook установлен!")

if __name__ == "__main__":
    asyncio.run(main())
