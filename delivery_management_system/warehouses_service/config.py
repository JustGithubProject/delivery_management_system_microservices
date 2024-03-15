import os

from dotenv import load_dotenv


env_file_path = '.env_db'

load_dotenv(dotenv_path=env_file_path)

#####################################################
WAREHOUSE_DB_USER = os.getenv("WAREHOUSE_DB_USER")  #
WAREHOUSE_DB_PASS = os.getenv("WAREHOUSE_DB_PASS")  #
WAREHOUSE_DB_NAME = os.getenv("WAREHOUSE_DB_NAME")  #
WAREHOUSE_DB_PORT = os.getenv("WAREHOUSE_DB_PORT")  #
WAREHOUSE_DB_HOST = os.getenv("WAREHOUSE_DB_HOST")  #
#####################################################



