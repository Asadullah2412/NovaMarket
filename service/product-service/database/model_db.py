from sqlalchemy import Boolean,Column,ForeignKey,Integer,String
from sqlalchemy.orm import Mapped, mapped_column
from  database.database import Base

class User(Base):
    __tablename__ = "users"

    id : Mapped[int]= mapped_column(Integer,primary_key=True,index=True)
    user_name:Mapped[str] = mapped_column(String)


class Product(Base):
    __tablename__ = "products"

    id : Mapped[int]= mapped_column(Integer,primary_key=True,index=True)
    product_name:Mapped[str] = mapped_column(String)

