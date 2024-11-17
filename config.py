
from dotenv import load_dotenv
from os import environ

load_dotenv()

API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']
MONGO_URI = environ.get('MONGO_URI', "")
STOCK_API_KEY = environ.get('STOCK_API_KEY', "")
PORT = environ.get("PORT", "8080")
