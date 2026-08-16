from sqlalchemy import Boolean,Column,ForeignKey,Integer,String
from sqlalchemy.orm import Mapped, mapped_column
from  database.database import Base



class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int]= mapped_column(Integer,primary_key=True,index=True)
    product_id : Mapped[int]= mapped_column(Integer)
    user_id : Mapped[int]= mapped_column(Integer)
    

