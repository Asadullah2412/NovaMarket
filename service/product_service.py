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

@ProductsRouter.delete('/delete_products')
def delete_product(product_id: int,):
    return products.remove_order(order_id=product_id)
