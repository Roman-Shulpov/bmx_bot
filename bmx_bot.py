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
from aiogram.fsm.storage.memory import MemoryStorage

from handlers.video_photo import register_handlers

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Регистрируем хэндлеры
register_handlers(dp)

app = FastAPI()


# FastAPI webhook handler
@app.post("/webhook")
async def webhook_handler(request: Request):
    update = types.Update.model_validate(await request.json(), context={"bot": bot})
    await dp.feed_update(bot, update)
    return {"ok": True}


@app.on_event("startup")
async def on_startup():
    webhook_url = os.getenv("RENDER_EXTERNAL_URL") + "/webhook"
    await bot.set_webhook(webhook_url)


@app.on_event("shutdown")
async def on_shutdown():
    await bot.delete_webhook()
    await bot.session.close()
