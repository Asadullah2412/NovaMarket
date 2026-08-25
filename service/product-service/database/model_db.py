from sqlalchemy import Boolean,Column,ForeignKey,Integer, Numeric,String
from sqlalchemy.orm import Mapped, mapped_column
from  database.database import Base

class Product(Base):
    __tablename__ = "products"

    id : Mapped[int]= mapped_column(Integer,primary_key=True,index=True)
    title:Mapped[str] = mapped_column(String,index=True)
    description: Mapped[str] = mapped_column()
    price:Mapped[float] = mapped_column(Numeric(10,2))
    quantity:Mapped[int] = mapped_column(default=0)
    seller_name:Mapped[str] = mapped_column(index=True)
    

