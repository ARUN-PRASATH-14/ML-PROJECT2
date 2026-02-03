import os
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["ai_career_db"]
collection = db["career_searches"]

def store_result(input_text, ai_output):
    collection.insert_one({
        "input": input_text,
        "result": ai_output,
        "timestamp": datetime.utcnow()
    })
