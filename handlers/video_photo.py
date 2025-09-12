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


from aiogram import types, Dispatcher

def register_handlers(dp: Dispatcher, bot, VIDEO_THREAD_ID, PHOTO_THREAD_ID):

    @dp.message_handler(content_types=types.ContentType.VIDEO)
    async def handle_video(message: types.Message):
        if message.chat.id != VIDEO_THREAD_ID:
            return
        # Видео есть — ничего не удаляем
        # Если нужен доп. функционал, добавь здесь

    @dp.message_handler(content_types=types.ContentType.PHOTO)
    async def handle_photo(message: types.Message):
        if message.chat.id != PHOTO_THREAD_ID:
            return
        # Фото есть — ничего не удаляем

    # Удаляем пустые сообщения в видео-топике
    @dp.message_handler(lambda m: m.chat.id == VIDEO_THREAD_ID)
    async def delete_empty_video(message: types.Message):
        if not message.video:
            await message.delete()

    # Удаляем пустые сообщения в фото-топике
    @dp.message_handler(lambda m: m.chat.id == PHOTO_THREAD_ID)
    async def delete_empty_photo(message: types.Message):
        if not message.photo:
            await message.delete()
