from typing import List

from fastapi import APIRouter
from model.products import Products_Manager
from pydantic import BaseModel


class ProductCreate(BaseModel):
    product_id: int
    product_name: str
    # products: List[str]  

    
products = Products_Manager()

    
ProductsRouter = APIRouter()

@ProductsRouter.get('/all_products')
def all_products():
    return products.show_products()

@ProductsRouter.post('/add_products')
def add_new_product(product_data: ProductCreate):
    result = products.add_product(
        product_name=product_data.product_name,
        product_id=product_data.product_id
    )
    return result

@ProductsRouter.put('/update_product')
def update_user(product_data: ProductCreate):
    result = products.update_user(new_user_name=product_data.user_name,user_id=product_data.user_id)
    return result

@ProductsRouter.get('/get_product')
def get_user(product_id):
    return products.get_product(product_id)

@ProductsRouter.delete('/delete_products')
def delete_product(product_id: int,):
    return products.remove_order(order_id=product_id)
