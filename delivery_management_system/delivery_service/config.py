import os

from dotenv import load_dotenv


env_file_path = '.env_db'

load_dotenv(dotenv_path=env_file_path)

###################################################
DELIVERY_DB_USER = os.getenv("DELIVERY_DB_USER")  #
DELIVERY_DB_PASS = os.getenv("DELIVERY_DB_PASS")  #
DELIVERY_DB_NAME = os.getenv("DELIVERY_DB_NAME")  #
DELIVERY_DB_PORT = os.getenv("DELIVERY_DB_PORT")  #
DELIVERY_DB_HOST = os.getenv("DELIVERY_DB_HOST")  #
###################################################

