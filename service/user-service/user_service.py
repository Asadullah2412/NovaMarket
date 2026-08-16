from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
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
def all_users(db: db_dependency):
    # Use the injected 'db' directly instead of 'with Session()'
    users = db.scalars(select(model_db.User)).all()
    return users


# add new user
@UserRouter.post('/users')
async def add_new_user(user_data :UserCreate,db:db_dependency):
    existing_user = db.scalars(select(model_db.User).where(model_db.User.id == user_data.user_id)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Already registered")
    
    db_user = model_db.User(id=user_data.user_id,user_name=user_data.user_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    
# update user
@UserRouter.put('/users/{user_id}')
def update_user(user_data :UserCreate,db:db_dependency):
    user = db.get(model_db.User,user_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.user_name = user_data.user_name
    db.commit()
    db.refresh(user)
    return user

# get a specific user
@UserRouter.get('/users/{user_id}')
def get_user(user_id,db:db_dependency):
    user = db.get(model_db.User,user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user



# delete user
@UserRouter.delete('/users/{user_id}')
def delete_user(user_data:UserCreate,db:db_dependency):
    user = db.get(model_db.User,user_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return None
