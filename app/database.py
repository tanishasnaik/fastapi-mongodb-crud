import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_URL = os.getenv("MONGO_URL")
print("Connecting to MongoDB at:", MONGO_URL)

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client["mydatabase"]
collection = db["users"]
