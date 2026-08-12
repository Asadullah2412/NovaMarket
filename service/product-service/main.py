# product microservice ⚠️⚠️
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from product_service import ProductsRouter




app = FastAPI(title="Product Inventory Service API",
    description="This service manages product catalogs, updates pricing, and tracks physical stock levels.",
    version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




app.include_router(router=ProductsRouter)



# uvicorn main:app --reload --port 8002
# to run