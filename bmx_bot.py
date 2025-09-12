import os
import asyncio
from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

# === Конфиг ===
BOT_TOKEN = "7976564635:AAGr4yMj4jDk5Lu6wam9JOfvkSrwHw0eYzg"
APP_URL = "https://bmx-bot-hual.onrender.com"  # твой Render URL
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"{APP_URL}{WEBHOOK_PATH}"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
app = FastAPI()


# === Хэндлеры бота ===
@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(f"Ты написал: {message.text}")


# === Webhook ===
@app.on_event("startup")
async def on_startup():
    # Убираем старый webhook (на всякий случай)
    await bot.delete_webhook(drop_pending_updates=True)
    # Ставим новый
    await bot.set_webhook(WEBHOOK_URL)
    print(f"Webhook установлен: {WEBHOOK_URL}")


@app.on_event("shutdown")
async def on_shutdown():
    await bot.session.close()


# === Подключаем aiogram к FastAPI ===
SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path=WEBHOOK_PATH)


# === Запуск локально (polling) ===
if __name__ == "__main__":
    import uvicorn

    # Если запускаем локально, то polling
    async def main():
        print("Запуск бота в режиме polling...")
        await dp.start_polling(bot)

    if os.getenv("RENDER") == "true":
        # Render запускает через uvicorn
        uvicorn.run("bmx_bot:app", host="0.0.0.0", port=10000, reload=False)
    else:
        asyncio.run(main())
