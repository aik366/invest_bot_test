from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("T_BANK_TOKEN")

if not TOKEN:
    raise RuntimeError("Не найден T_BANK_TOKEN в .env")
