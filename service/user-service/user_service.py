from fastapi import APIRouter, Depends
from model.users import User_manager
from pydantic import BaseModel
from typing import List
from database import model_db
from database.user_db import engine,SessionLocal
from sqlalchemy.orm import Session
from typing import Annotated
class UserCreate(BaseModel):
    user_id: int
    user_name: str
    # products: List[str]  

users = User_manager()
model_db.Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]

UserRouter = APIRouter()
#  get all the users 
@UserRouter.get('/users')
def all_users():
    return users.show_users()

# add new user
@UserRouter.post('/users')
async def add_new_user(user_data :UserCreate,db:db_dependency):
    # result = users.add_user(name=user_data.user_name,user_id=user_data.user_id)
    db_user = model_db.User(id=user_data.user_id,user_name=user_data.user_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    # return "user created"

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
