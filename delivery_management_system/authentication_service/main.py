from fastapi import FastAPI

from auth.routers import user_router


authentication_app = FastAPI()

authentication_app.include_router(user_router)







