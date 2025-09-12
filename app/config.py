import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Должно быть HTTPS

CHAT_ID_1 = int(os.getenv("CHAT_ID_1"))
CHAT_ID_2 = int(os.getenv("CHAT_ID_2"))
ALLOWED_CHAT_IDS = {CHAT_ID_1, CHAT_ID_2}
