from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types
import asyncio
import os

BOT_TOKEN = "7976564635:AAGr4yMj4jDk5Lu6wam9JOfvkSrwHw0eYzg"
WEBHOOK_PATH = f"/webhook/{BOT_TOKEN}"
WEBHOOK_URL = f"https://bmx-bot-hual.onrender.com{WEBHOOK_PATH}"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

app = FastAPI()

# пример хендлера
@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

@app.post(WEBHOOK_PATH)
async def telegram_webhook(request: Request):
    update = types.Update(**await request.json())
    await dp.feed_update(update)
    return {"ok": True}

async def on_startup():
    await bot.delete_webhook()
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown():
    await bot.delete_webhook()
    await bot.session.close()

app.add_event_handler("startup", on_startup)
app.add_event_handler("shutdown", on_shutdown)
