import os
from aiogram import Dispatcher, types

VIDEO_THREAD_ID = int(os.getenv("VIDEO_THREAD_ID"))
PHOTO_THREAD_ID = int(os.getenv("PHOTO_THREAD_ID"))

def register_handlers(dp: Dispatcher):
    @dp.message()
    async def check_video_photo(message: types.Message):
        # --- Видео раздел ---
        if message.chat.id == VIDEO_THREAD_ID:
            if not message.video and not (message.document and message.document.mime_type.startswith("video/")):
                try:
                    await message.delete()
                except Exception:
                    pass
                return

        # --- Фото раздел ---
        elif message.chat.id == PHOTO_THREAD_ID:
            if not message.photo:
                try:
                    await message.delete()
                except Exception:
                    pass
                return
