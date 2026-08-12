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

@OrderRouter.get('/all_orders')
def all_orders():
    return orders.show_orders()

@OrderRouter.post('/add_order')
def add_new_order(order_data: OrderCreate):
    result = orders.add_order(
        order_id=order_data.order_id, 
        user_name=order_data.user_name,
        products=order_data.products
    )
    return result


@OrderRouter.put('/update_order')
def update_user(order_data:OrderCreate):
    result = orders.update_order(order_id=order_data.order_id,new_products=order_data.products)
    return result

@OrderRouter.get('/get_order')
def get_user(order_id):
    return orders.get_product(order_id)

@OrderRouter.delete('/delete_order')
def delete_order(order_id: int,):
    return orders.remove_order(order_id=order_id)
