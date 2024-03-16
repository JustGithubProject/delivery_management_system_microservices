from sqlalchemy import create_engine

from sqlalchemy.orm import (
    sessionmaker
)

from warehouses_service.config import (
    WAREHOUSE_DB_USER,
    WAREHOUSE_DB_PASS,
    WAREHOUSE_DB_NAME,
    WAREHOUSE_DB_PORT,
    WAREHOUSE_DB_HOST
)


engine = create_engine(
    f"postgresql+psycopg2://"
    f"{WAREHOUSE_DB_USER}:{WAREHOUSE_DB_PASS}@{WAREHOUSE_DB_HOST}:{WAREHOUSE_DB_PORT}/{WAREHOUSE_DB_NAME}"
)

Session = sessionmaker(engine)

