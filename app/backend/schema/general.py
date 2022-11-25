from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import List


class User(BaseModel):
    email: str
    creation_date: datetime

    def helper(data) -> dict:
        """Function in charge of parsing mongo response into dict
        """
        return {
            "_id": str(data["_id"]),
            "email": data["email"],
            "creation_date": data["creation_date"]
        }


class Status(str, Enum):
    CREATED = "0"
    RUNNING = "1"
    FINISHED = "2"


class Game(BaseModel):
    user_id: str
    last_word: str
    history: List[str]
    total_score: int
    creation_date: datetime
    update: bool
    update_time: datetime
    status: Status

    def helper(data) -> dict:
        """Function in charge of parsing mongo response into dict
        """
        return {
            "_id": str(data["_id"]),
            "user_id": data["user_id"],
            "last_word": data["last_word"],
            "history": data["history"],
            "total_score": data["total_score"],
            "creation_date": data["creation_date"],
            "update": data["update"],
            "update_time": data["update_time"],
            "status": data["status"]
        }
