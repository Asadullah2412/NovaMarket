from fastapi import APIRouter
from model.users import Users

users = Users()

UserRouter = APIRouter()

@UserRouter.get('/all_users')
def all_users():
    return users.show_users()

@UserRouter.post('/add_user')
def add_new_user(name: str, id: int):
    return users.add_user(name=name,id=id)
