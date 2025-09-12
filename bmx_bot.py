import logging
from fastapi import FastAPI
from aiogram import Bot, Dispatcher, types
from aiogram.webhook.fastapi import SimpleRequestHandler, setup_application

# === Твои данные ===
BOT_TOKEN = "7976564635:AAGr4yMj4jDk5Lu6wam9JOfvkSrwHw0eYzg"
APP_URL = "https://bmx-bot-hual.onrender.com"
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"{APP_URL}{WEBHOOK_PATH}"

# Логирование
logging.basicConfig(level=logging.INFO)

# Инициализация
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
app = FastAPI()


# === Хендлеры ===
@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(f"Привет 👋 Ты написал: {message.text}")


# === Webhook ===
SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path=WEBHOOK_PATH)
setup_application(app, dp, bot=bot, path=WEBHOOK_PATH)


# === Автоматическая настройка вебхука ===
@app.on_event("startup")
async def on_startup():
    logging.info("Устанавливаем вебхук...")
    await bot.set_webhook(WEBHOOK_URL)
    logging.info(f"Вебхук установлен: {WEBHOOK_URL}")


@app.on_event("shutdown")
async def on_shutdown():
    logging.info("Удаляем вебхук...")
    await bot.delete_webhook()
    logging.info("Вебхук удалён")
