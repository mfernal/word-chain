from fastapi import APIRouter
from fastapi import HTTPException
from datetime import datetime
from bson.objectid import ObjectId

from app.backend.schema.general import Game
from app.backend.crud import Crud
from app.backend.core.games import generate_new_word

router = APIRouter()


@router.get("/")
async def get_all_games() -> list:
    crud = Crud()
    data = []
    games = crud.games.find({})
    for game in await games.to_list(length=10):
        data.append(Game.helper(game))
    return data


@router.get("/{id}")
async def get_game_by_id(id: str) -> dict:
    crud = Crud()
    games = crud.games.find({
        "_id": ObjectId(id)
    })
    for game in await games.to_list(length=10):
        return Game.helper(game)


@router.post("/")
async def create_game(game: Game) -> dict:
    crud = Crud()
    data = await crud.games.insert_one(dict(game))
    new_data = await crud.games.find_one({
        "_id": data.inserted_id
    })
    return Game.helper(new_data)


@router.post("/play")
async def play(id: str, word: str, game: Game) -> dict:
    if word.lower() in game.history:
        raise HTTPException(status_code=400, detail="Word already used")
    game.history.append(word.lower())
    last_word = generate_new_word(word, game)
    game.last_word = last_word
    game.history.append(last_word)
    return game


@router.put("/")
async def modify_game_by_id(id: str, game: Game) -> dict:
    crud = Crud()
    game = dict(game)
    game.update({
        "update": True,
        "update_time": datetime.now()
    })
    if not game:
        raise HTTPException(status_code=500, detail="Internal Server Error")

    updated_data = await crud.games.update_one({
        "_id": ObjectId(id)
    }, {
        "$set": game
    })
    if not updated_data:
        raise HTTPException(status_code=404, detail="Item not found")
    return game


@router.delete("/")
async def delete_game_by_id():
    pass
