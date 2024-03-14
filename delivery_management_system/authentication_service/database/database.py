from sqlalchemy import create_engine

from sqlalchemy.orm import (
    sessionmaker
)

from config import (
    AUTH_DB_USER,
    AUTH_DB_PASS,
    AUTH_DB_NAME,
    AUTH_DB_PORT,
    AUTH_DB_HOST
)


engine = create_engine(
    f"postgresql+psycopg2://{AUTH_DB_USER}:{AUTH_DB_PASS}@{AUTH_DB_HOST}:{AUTH_DB_PORT}/{AUTH_DB_NAME}"
)

Session = sessionmaker(engine)
