from fastapi import FastAPI

from auth.routers import user_router


# An instance of FastAPI (for authentication service)
authentication_app = FastAPI()

# Attaching routers to authentication_app
authentication_app.include_router(user_router)







