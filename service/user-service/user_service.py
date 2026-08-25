from fastapi import APIRouter, HTTPException,Depends,status
from sqlalchemy import select
from pydantic import BaseModel
from database.dependencies import model_db
from database.dependencies import db_dependency
from auth.utils import get_password_hash , create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from auth.authentication import authenticate_user

class UserCreate(BaseModel):
    # user_id: int
    user_name: str
    password:str
    role:str



class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

    # products: List[str]  

UserRouter = APIRouter()
#  get all the users 
@UserRouter.get('/users')
def all_users(db: db_dependency):
    # Use the injected 'db' directly instead of 'with Session()'
    users = db.scalars(select(model_db.User)).all()
    return users


# add new user
@UserRouter.post('/users')
async def signup(user_data :UserCreate,db:db_dependency):
    existing_user = db.scalars(select(model_db.User).where(model_db.User.user_name == user_data.user_name)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Already registered")
    hashed_password = get_password_hash(user_data.password)
    db_user = model_db.User(hashed_password = hashed_password,
                            user_name=user_data.user_name,
                            role = user_data.role,
                            is_active=True,
                            )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



@UserRouter.post("/users/token",response_model=Token)
def login_for_access_token(db:db_dependency,form_data:OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db,form_data.username,form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub":user.user_name, "role": user.role})
    return {'access_token':access_token,"token_type":"bearer"}


    
# update user
@UserRouter.put('/users/{user_id}') 
def update_user(user_data :UserCreate,db:db_dependency):
    user = db.get(model_db.User,user_data.user_name)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.user_name = user_data.user_name
    db.commit()
    db.refresh(user)
    return user

# get a specific user
@UserRouter.get('/users/{user_name}')
def get_user(user_name,db:db_dependency):
    user = db.get(model_db.User,user_name)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user



# delete user
@UserRouter.delete('/users/{user_id}')
def delete_user(user_data:UserCreate,db:db_dependency):
    user = db.get(model_db.User,user_data.user_name)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return None
