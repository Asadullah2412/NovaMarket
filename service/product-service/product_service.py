from typing import List
from sqlalchemy import select
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from database.dependencies import model_db
from database.dependencies import db_dependency

class ProductCreate(BaseModel):
    product_id: int
    product_name: str
    # products: List[str]  

    
# products = Products_Manager()

    
ProductsRouter = APIRouter()

# get all products
@ProductsRouter.get('/products')
def all_products(db:db_dependency):
    products = db.scalars(select(model_db.Product)).all()
    return products

# add product
@ProductsRouter.post('/products/')
def add_new_product(product_data: ProductCreate,db:db_dependency):
    existing_product = db.scalars(select(model_db.Product).where(model_db.Product.id == product_data.product_id)).first()
    if existing_product:
            raise HTTPException(status_code=400, detail="Already registered")
        
    db_product = model_db.Product(id=product_data.product_id,product_name=product_data.product_name)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
   

# update product
@ProductsRouter.put('/products/{product_id}')
def update_product(product_data: ProductCreate,db:db_dependency):
    product = db.get(model_db.Product,product_data.product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product.product_name = product_data.product_name
    db.commit()
    db.refresh(product)
    return product

# get single product
@ProductsRouter.get('/products/{product_id}')
def get_product(product_id:int,db:db_dependency):
    product = db.get(model_db.Product,product_id)
    if not product:
        raise HTTPException(status_code=404, detail="product not found")
    return product

#  delete product
@ProductsRouter.delete('/products/{product_id}')
def delete_product(product_id: int,db:db_dependency):
    product = db.get(model_db.Product,product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return None
