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
from aiogram import Bot, types

async def check_message(bot: Bot, update: types.Update):
    message = update.message
    if not message:
        return

    # Если видео раздел
    if message.video or message.document and message.document.mime_type.startswith("video"):
        return
    # Если фото раздел
    if message.photo:
        return

    # Удаляем пустое сообщение
    try:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    except Exception:
        pass

