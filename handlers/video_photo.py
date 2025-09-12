# ========================РАБОТАЕТ ВРОДЕ НО НЕ ТАК===========================================
# import os
# from aiogram import Dispatcher, types

# VIDEO_THREAD_ID = int(os.getenv("VIDEO_THREAD_ID"))
# PHOTO_THREAD_ID = int(os.getenv("PHOTO_THREAD_ID"))

# def register_handlers(dp: Dispatcher):
#     @dp.message()
#     async def check_video_photo(message: types.Message):
#         # --- Видео раздел ---
#         if message.chat.id == VIDEO_THREAD_ID:
#             if not message.video and not (message.document and message.document.mime_type.startswith("video/")):
#                 try:
#                     await message.delete()
#                 except Exception:
#                     pass
#                 return

#         # --- Фото раздел ---
#         elif message.chat.id == PHOTO_THREAD_ID:
#             if not message.photo:
#                 try:
#                     await message.delete()
#                 except Exception:
#                     pass
#                 return
# ========================РАБОТАЕТ ВРОДЕ НО НЕ ТАК===========================================
from aiogram import Router, F
from aiogram.types import Message

import os

CHAT_ID_1 = int(os.getenv("CHAT_ID_1"))
CHAT_ID_2 = int(os.getenv("CHAT_ID_2"))
ALLOWED_CHAT_IDS = {CHAT_ID_1, CHAT_ID_2}

router = Router()


@router.message(F.chat.id.in_(ALLOWED_CHAT_IDS))
async def handle_media(message: Message):
    # Если есть фото или видео - пропускаем
    if message.photo or message.video:
        return
    # иначе удаляем
    await message.delete()
