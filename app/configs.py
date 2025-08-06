import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8000))
ENV = os.getenv("ENV", 'DEV')
DB_URL = os.getenv("DB_URL")
THIRD_PARTY_PRODUCTS = os.getenv("THIRD_PARTY_PRODUCTS")
API_RATE_LIMIT = os.getenv("API_RATE_LIMIT", "60/minute")