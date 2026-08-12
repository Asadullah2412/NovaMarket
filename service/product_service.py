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

# get all products
@ProductsRouter.get('/products')
def all_products():
    return products.show_products()

# add product
@ProductsRouter.post('/products/')
def add_new_product(product_data: ProductCreate):
    result = products.add_product(
        product_name=product_data.product_name,
        product_id=product_data.product_id
    )
    return result

# update product
@ProductsRouter.put('/products/{product_id}')
def update_product(product_data: ProductCreate):
    result = products.update_user(new_user_name=product_data.user_name,user_id=product_data.user_id)
    return result

# get single product
@ProductsRouter.get('/products/{product_id}')
def get_product(product_id):
    return products.get_product(product_id)

#  delete product
@ProductsRouter.delete('/products/{product_id}')
def delete_product(product_id: int,):
    return products.remove_order(order_id=product_id)
