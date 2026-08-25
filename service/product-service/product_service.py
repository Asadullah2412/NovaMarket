from typing import List
from sqlalchemy import select
from fastapi import APIRouter, HTTPException , Depends,status
from pydantic import BaseModel, Field
from auth.auth import require_seller
from database.dependencies import model_db
from database.dependencies import db_dependency
from database import model_db

class ProductBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: str
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=0)

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    seller_name: str

    class Config:
        from_attributes = True


    
ProductsRouter= APIRouter()

@ProductsRouter.get("/products", response_model=List[ProductResponse])
def browse_products(db: db_dependency):
    """Accessible by anyone (Buyers/Sellers) to browse inventory listings"""
    products = db.scalars(select(model_db.Product)).all()
    return products

@ProductsRouter.get("/products/{product_id}", response_model=ProductResponse)
def read_single_product(product_id: int, db: db_dependency):
    product = db.get(model_db.Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


# --- 🏢 SELLER CONTROL LOGIC (Protected CRUD) ---

@ProductsRouter.post("/products", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(
    product_data: ProductCreate, 
    db: db_dependency, 
    seller_payload: dict = Depends(require_seller)
):
    """Creates a new listing. seller_name is extracted safely from the token payload."""
    new_product = model_db.Product(
        title=product_data.title,
        description=product_data.description,
        price=product_data.price,
        quantity=product_data.quantity,
        seller_name=seller_payload.get("sub") # Inferred username
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@ProductsRouter.put("/products/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int, 
    updated_data: ProductCreate, 
    db: db_dependency, 
    seller_payload: dict = Depends(require_seller)
):
    product = db.get(model_db.Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product entity not found")
    
    # Security Check: Ensure seller owns this listing before modifying it
    if product.seller_name != seller_payload.get("sub"):
        raise HTTPException(status_code=403, detail="You do not own this resource block.")
        
    product.title = updated_data.title
    product.description = updated_data.description
    product.price = updated_data.price
    product.quantity = updated_data.quantity
    
    db.commit()
    db.refresh(product)
    return product

@ProductsRouter.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    product_id: int, 
    db: db_dependency, 
    seller_payload: dict = Depends(require_seller)
):
    product = db.get(model_db.Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product entity not found")
        
    if product.seller_name != seller_payload.get("sub"):
        raise HTTPException(status_code=403, detail="De-registration access denied.")
        
    db.delete(product)
    db.commit()
    return {"detail": "Product erased successfully"}