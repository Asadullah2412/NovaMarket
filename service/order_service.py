from typing import List

from fastapi import APIRouter
from model.orders import Order_manager
from pydantic import BaseModel

class OrderCreate(BaseModel):
    order_id: int
    user_name: str
    user_id : int
    products: List[str]  

    
orders = Order_manager()

OrderRouter = APIRouter()

#  get all products
@OrderRouter.get('/orders')
def all_orders():
    return orders.show_orders()

# add new products
@OrderRouter.post('/orders')
def add_new_order(order_data: OrderCreate):
    result = orders.add_order(
        order_id=order_data.order_id, 
        user_name=order_data.user_name,
        products=order_data.products
    )
    return result

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
