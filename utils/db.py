
from pymongo import MongoClient
import config

client = MongoClient(config.MONGO_URI)
db = client.stock_bot

def save_query(user_id, query):
    db.queries.insert_one({"user_id": user_id, "query": query})
