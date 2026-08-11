from fastapi import APIRouter
from model.users import User_manager
from pydantic import BaseModel
from typing import List
class UserCreate(BaseModel):
    user_id: int
    user_name: str
    # products: List[str]  

users = User_manager()

UserRouter = APIRouter()

@UserRouter.get('/all_users')
def all_users():
    return users.show_users()

@UserRouter.post('/add_user')
def add_new_user(user_data :UserCreate):
    result = users.add_user(name=user_data.user_name,user_id=user_data.user_id)
    return result
    


@UserRouter.delete('/remove_user')
def delete_user(name: str,):
    return users.remove_user(name)
