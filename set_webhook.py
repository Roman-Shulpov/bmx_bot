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


async def set_webhook():
    token = os.getenv("BOT_TOKEN")
    bot = Bot(token=token)

    webhook_url = os.getenv("RENDER_EXTERNAL_URL") + "/webhook"
    await bot.set_webhook(webhook_url)

    print(f"Webhook установлен: {webhook_url}")
    await bot.session.close()


if __name__ == "__main__":
    asyncio.run(set_webhook())
