
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
MONGO_URI = os.getenv("MONGO_URI")
