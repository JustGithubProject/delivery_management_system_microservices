from sqlalchemy import (
    create_engine
)
from sqlalchemy.orm import sessionmaker

from ..config import (
    ORDER_DB_HOST,
    ORDER_DB_USER,
    ORDER_DB_PASS,
    ORDER_DB_PORT,
    ORDER_DB_NAME
)

engine = create_engine(
    f"postgresql+psycopg2://{ORDER_DB_USER}:{ORDER_DB_PASS}@{ORDER_DB_HOST}:{ORDER_DB_PORT}/{ORDER_DB_NAME}"
)

Session = sessionmaker(engine)