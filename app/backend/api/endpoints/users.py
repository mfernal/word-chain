from fastapi import APIRouter
from fastapi import HTTPException
from datetime import datetime
from app.backend.crud import Crud
from app.backend.schema.general import User
from bson.objectid import ObjectId

router = APIRouter()


@router.get("/")
async def get_all_users() -> dict:
    crud = Crud()
    data = []
    users = crud.users.find({})
    for user in await users.to_list(length=10):
        data.append(User.helper(user))
    return data


@router.get("/{id}")
async def get_user_by_id(id: str) -> dict:
    crud = Crud()
    data = await crud.users.find_one({
        "_id": ObjectId(id)
    })
    return User.helper(data)


@router.get("/by_email")
async def get_user_by_email(email: str) -> dict:
    crud = Crud()
    data = await crud.users.find_one({
        "email": email
    })
    return User.helper(data)


@router.post("/")
async def create_user(user: User) -> dict:
    crud = Crud()
    data = await crud.users.insert_one(dict(user))
    new_data = await crud.users.find_one({
        "_id": data.inserted_id
    })
    return User.helper(new_data)


@router.put("/")
async def modify_user_by_id(id: str, user: User) -> dict:
    crud = Crud()
    user = dict(user)
    user.update({
        "update": True,
        "update_time": datetime.now()
    })
    if not user:
        raise HTTPException(status_code=500, detail="Internal Server Error")

    updated_data = await crud.users.update_one({
        "_id": ObjectId(id)
    }, {
        "$set": user
    })

    if not updated_data:
        raise HTTPException(status_code=404, detail="Item not found")
    return user


@router.delete("/")
async def delete_user_by_id():
    pass
