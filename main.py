# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from service.user_service import UserRouter
# from service.order_service import OrderRouter
# from service.product_service import ProductsRouter



# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Adjust this in production
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )



# app.include_router(router=UserRouter)
# app.include_router(router=ProductsRouter)
# app.include_router(router=OrderRouter)


# # uvicorn main:app --reload
# # to run