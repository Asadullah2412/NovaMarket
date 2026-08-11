from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from service.user_service import UserRouter



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(router=UserRouter)


# uvicorn main:app --reload
# to run