from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import (
    DELIVERY_DB_USER,
    DELIVERY_DB_PASS,
    DELIVERY_DB_NAME,
    DELIVERY_DB_PORT,
    DELIVERY_DB_HOST
)

print(DELIVERY_DB_NAME)