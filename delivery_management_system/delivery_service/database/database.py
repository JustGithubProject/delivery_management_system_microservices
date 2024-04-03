from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import (
    DELIVERY_DB_USER,
    DELIVERY_DB_PASS,
    DELIVERY_DB_NAME,
    DELIVERY_DB_PORT,
    DELIVERY_DB_HOST
)


engine = create_engine(
    f"postgresql+psycopg2://{DELIVERY_DB_USER}:{DELIVERY_DB_PASS}@{DELIVERY_DB_HOST}:{DELIVERY_DB_PORT}/{DELIVERY_DB_NAME} "
)

Session = sessionmaker(engine)