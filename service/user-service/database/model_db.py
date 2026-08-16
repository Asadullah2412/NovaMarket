from sqlalchemy import Boolean,Column,ForeignKey,Integer,String
from  database.user_db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    user_name = Column(String,index=True)