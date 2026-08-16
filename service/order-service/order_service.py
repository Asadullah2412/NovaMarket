from typing import List
import httpx

from fastapi import APIRouter, HTTPException , status
from sqlalchemy import select
# from model.orders import Order_manager

from database.dependencies import model_db
from database.dependencies import db_dependency
from pydantic import BaseModel

class OrderCreate(BaseModel):
    order_id: int
    user_name: str
    user_id : int
    product_id: int 


OrderRouter = APIRouter()

#  get all products
@OrderRouter.get('/orders')
def all_orders(db:db_dependency):
    orders = db.scalars(select(model_db.Product)).all()
    return orders

# add new products
@OrderRouter.post('/orders')
async def add_new_order(order_data: OrderCreate,db:db_dependency):
    # check first if the products exists 
    # target the url of product service
    product_service_url = f"http://localhost:8002/products/{order_data.product_id}"
    user_service_url = f"http://localhost:8001/users/{order_data.user_id}"
    #  open an http cl;ient session to make the request 
    async with httpx.AsyncClient() as client:
        try:
            product_response = await client.get(product_service_url)
            user_response = await client.get(user_service_url)
        except httpx.RequestError:
            # Safely handle the error if the Product Service is completely turned off
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Product service is currently offline."
            )
    # check what the product service respomded with 
    if product_response.status_code == 404:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Product with ID {order_data.product_id} does not exist!"
        )
    elif user_response.status_code == 404:
         raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"user with ID {order_data.user_id} does not exist!"
                )
    else:
       existing_order = db.scalars(select(model_db.Order).where(model_db.Order.id == order_data.order_id)).first()
    if existing_order:
                raise HTTPException(status_code=400, detail="Already registered")
               
    db_order = model_db.Order(id=order_data.order_id,product_id=order_data.product_id,user_id=order_data.user_id
                                 )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order
   

# update order
@OrderRouter.put('/orders/{order_id}')
def update_order(order_data:OrderCreate):
    result = orders.update_order(order_id=order_data.order_id,new_products=order_data.products)
    return result

# get single order
@OrderRouter.get('/orders/{order_id}')
def get_order(order_id):
    return orders.get_product(order_id)

# delete order
@OrderRouter.delete('/orders/{order_id}')
def delete_order(order_id: int,):
    return orders.remove_order(order_id=order_id)
