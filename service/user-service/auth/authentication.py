from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from auth.utils import verify_password, get_password_hash, create_access_token, SECRET_KEY, ALGORITHM
# from user_service import TokenData
# from model_d import User
from database.dependencies import model_db
from database.dependencies import db_dependency



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")



# def get_user(db: Session, username: str):
#     return db.query(User).filter(User.username == username).first()

def authenticate_user(db:db_dependency , username: str, password: str):
    user = db.get(model_db.User,username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

# def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(username=username)
#     except JWTError:
#         raise credentials_exception
#     user = get_user(db, username=token_data.username)
#     if user is None:
#         raise credentials_exception
#     return user