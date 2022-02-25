import os

import motor.motor_asyncio
from fastapi_users.db import MongoDBUserDatabase

from app.models import UserDB

#DATABASE_URL = os.environ["mongodb+srv://dbUser:UtCgMNghTUiNyKgM@myfirstcluster.py8c0.mongodb.net/MyFirstCluster"]
client = motor.motor_asyncio.AsyncIOMotorClient(
    "mongodb+srv://dbUser:UtCgMNghTUiNyKgM@myfirstcluster.py8c0.mongodb.net/MyFirstCluster", uuidRepresentation="standard"
)
db = client["NewApp"]
collection = db["users"]


async def get_user_db():
    yield MongoDBUserDatabase(UserDB, collection)