from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI

MONGO_URI = "mongodb+srv://rudrapatel0214:rp12345@cluster0.ngazw36.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "Cluster0"

client = AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]
collection = database["users"]

async def get_database():
    return database