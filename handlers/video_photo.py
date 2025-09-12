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
import os
from aiogram import Dispatcher, types


async def filter_messages(message: types.Message):
    chat_ids = [int(os.getenv("CHAT_ID_1")), int(os.getenv("CHAT_ID_2"))]

    # если сообщение не из разрешённых чатов
    if message.chat.id not in chat_ids:
        return

    # удаляем всё, что не фото/видео
    if not (message.photo or message.video):
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


def register_handlers(dp: Dispatcher):
    dp.message.register(filter_messages)
