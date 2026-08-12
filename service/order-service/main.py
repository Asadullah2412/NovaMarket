# order microservice⚠️⚠️
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from order_service import OrderRouter



app = FastAPI(title="Order Processing Service API",
    description="This service coordinates checkouts, manages shopping carts, and processes purchases.",
    version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(router=OrderRouter)



# uvicorn main:app --reload --port 8003
# to run