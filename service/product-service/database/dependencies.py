
from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from database import model_db
from database.database import SessionLocal, engine, Base

model_db.Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]