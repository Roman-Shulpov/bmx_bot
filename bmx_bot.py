# ========================РАБОТАЕТ ВРОДЕ НО НЕ ТАК===========================================

# import os
# from fastapi import FastAPI, Request
# from aiogram import Bot, Dispatcher, types
# from aiogram.types import Update
# from handlers import video_photo

# TOKEN = os.getenv("TOKEN")
# bot = Bot(token=TOKEN, parse_mode="HTML")
# dp = Dispatcher()
# video_photo.register_handlers(dp)

# app = FastAPI()

# @app.post("/webhook")
# async def telegram_webhook(req: Request):
#     data = await req.json()
#     update = Update(**data)
#     await dp.update_router.dispatch(update)
#     return {"ok": True}

# ========================РАБОТАЕТ ВРОДЕ НО НЕ ТАК===========================================

import os
from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types
from handlers import video_photo

BOT_TOKEN = os.getenv("BOT_TOKEN")
VIDEO_THREAD_ID = int(os.getenv("VIDEO_THREAD_ID"))
PHOTO_THREAD_ID = int(os.getenv("PHOTO_THREAD_ID"))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

app = FastAPI()

# Главная страница (для проверки deploy)
@app.get("/")
async def root():
    return {"message": "BMX Bot работает!"}

# Webhook Telegram
@app.post(f"/webhook/{BOT_TOKEN}")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = types.Update(**data)
    await dp.process_update(update)
    return {"ok": True}

# Регистрируем обработчики
video_photo.register_handlers(dp, bot, VIDEO_THREAD_ID, PHOTO_THREAD_ID)

