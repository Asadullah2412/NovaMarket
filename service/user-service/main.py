# User microservices ⚠️⚠️
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from user_service import UserRouter
# from database import model_db




app = FastAPI( title="User Management Service API",
    description="This service handles user registration, profiles, and authentication.",
    version="1.0.0")




app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(router=UserRouter)



# uvicorn main:app --reload --port 8001
# to run
