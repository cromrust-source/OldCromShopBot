import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))
SERVER_IP = os.getenv("SERVER_IP")
API_PORT = int(os.getenv("API_PORT", 1234))
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
