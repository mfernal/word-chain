import motor.motor_asyncio
from app.backend.core.settings import (MONGO_CONNECTION_STRING, MONGO_DATABASE_NAME, MONGO_USERS_COLLECTION, MONGO_GAMES_COLLECTION)


class Crud:
    def __init__(
        self,
    ):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(
            MONGO_CONNECTION_STRING
        )
        self.database = self.client[MONGO_DATABASE_NAME]
        self.users = self.database.get_collection(
            MONGO_USERS_COLLECTION
        )
        self.games = self.database.get_collection(
            MONGO_GAMES_COLLECTION
        )
