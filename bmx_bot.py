# bmx_bot.py
import logging
from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types
from aiogram.types import Update

TOKEN = "7976564635:AAGr4yMj4jDk5Lu6wam9JOfvkSrwHw0eYzg"
VIDEO_THREAD_ID = 4
PHOTO_THREAD_ID = 12

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=TOKEN)
dp = Dispatcher()

app = FastAPI()

# ------------------------------
# Проверка содержимого сообщений
# ------------------------------
def message_contains_image(msg: types.Message) -> bool:
    if msg.photo:
        return True
    if msg.document and msg.document.mime_type and msg.document.mime_type.startswith("image/"):
        return True
    return False

def message_contains_video(msg: types.Message) -> bool:
    if msg.video or msg.video_note or msg.animation:
        return True
    if msg.document and msg.document.mime_type and msg.document.mime_type.startswith("video/"):
        return True
    return False

# ------------------------------
# Фильтрация сообщений по топикам
# ------------------------------
@dp.message()
async def filter_by_thread(message: types.Message):
    thread_id = message.message_thread_id
    if thread_id is None:
        return
    try:
        if thread_id == VIDEO_THREAD_ID and not message_contains_video(message):
            await message.delete()
        elif thread_id == PHOTO_THREAD_ID and not message_contains_image(message):
            await message.delete()
    except Exception as e:
        logger.exception("Ошибка при обработке сообщения: %s", e)

# ------------------------------
# Webhook endpoint
# ------------------------------
@app.post(f"/webhook/{TOKEN}")
async def telegram_webhook(req: Request):
    data = await req.json()
    update = Update(**data)
    await dp.process_update(update)
    return {"ok": True}

# ------------------------------
# Startup / Shutdown
# ------------------------------
@app.on_event("startup")
async def on_startup():
    # НЕ устанавливаем webhook на старте Render
    logger.info("Приложение стартовало. Установите webhook один раз через set_webhook.py")

@app.on_event("shutdown")
async def on_shutdown():
    await bot.session.close()
