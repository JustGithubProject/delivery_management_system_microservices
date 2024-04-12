from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from delivery.routers import delivery_router

# An instance of FastAPI (for delivery service)
delivery_app = FastAPI()

# Attaching routers to delivery_app
delivery_app.include_router(delivery_router)

# CORS for frontend(soon)
origins = []
delivery_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)