from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from warehouse.routers import warehouse_router

# An instance of FastAPI (for warehouse service)
warehouse_app = FastAPI()

# Attaching routers to warehouse_app
warehouse_app.include_router(warehouse_router)

# CORS for frontend(soon)
origins = []
warehouse_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
