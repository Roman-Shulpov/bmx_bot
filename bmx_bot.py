import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentType
from aiogram.filters import Filter

# Получаем переменные из Environment Variables
TOKEN = os.getenv("TOKEN")
VIDEO_THREAD_ID = int(os.getenv("VIDEO_THREAD_ID"))  # топик для видео
PHOTO_THREAD_ID = int(os.getenv("PHOTO_THREAD_ID"))  # топик для фото

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher()

# Фильтр для сообщений без видео в видео-топике
class NoVideoFilter(Filter):
    async def __call__(self, message: types.Message) -> bool:
        return message.chat.id == VIDEO_THREAD_ID and not message.video

# Фильтр для сообщений без фото в фото-топике
class NoPhotoFilter(Filter):
    async def __call__(self, message: types.Message) -> bool:
        return message.chat.id == PHOTO_THREAD_ID and not message.photo

# Хэндлер для удаления сообщений без видео
@dp.message(NoVideoFilter())
async def delete_no_video(message: types.Message):
    try:
        await message.delete()
    except Exception as e:
        print(f"Ошибка при удалении сообщения: {e}")

# Хэндлер для удаления сообщений без фото
@dp.message(NoPhotoFilter())
async def delete_no_photo(message: types.Message):
    try:
        await message.delete()
    except Exception as e:
        print(f"Ошибка при удалении сообщения: {e}")

# Запуск бота
async def main():
    try:
        print("Бот запущен...")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
