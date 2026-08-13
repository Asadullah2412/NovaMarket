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
#  get all the users 
@UserRouter.get('/users')
def all_users():
    return users.show_users()

# add new user
@UserRouter.post('/users')
def add_new_user(user_data :UserCreate):
    result = users.add_user(name=user_data.user_name,user_id=user_data.user_id)
    return result

# update euser
@UserRouter.put('/users/{user_id}')
def update_user(user_data :UserCreate):
    result = users.update_user(new_user_name=user_data.user_name,user_id=user_data.user_id)
    return result

# get a specific user
@UserRouter.get('/users/{user_id}')
def get_user(user_data:UserCreate):
    return users.get_user(user_data.user_id)

# delete user
@UserRouter.delete('/users/{user_id}')
def delete_user(name: str,):
    return users.remove_user(name)
