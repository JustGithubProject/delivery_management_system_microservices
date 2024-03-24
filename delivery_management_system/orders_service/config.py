import os

from dotenv import load_dotenv


load_dotenv(dotenv_path=".env")

###############################################################
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")                  #
JWT_REFRESH_SECRET_KEY = os.getenv("JWT_REFRESH_SECRET_KEY")  #
###############################################################

load_dotenv(".env_db")


#############################################
ORDER_DB_USER = os.getenv("ORDER_DB_USER")  #
ORDER_DB_PASS = os.getenv("ORDER_DB_PASS")  #
ORDER_DB_HOST = os.getenv("ORDER_DB_HOST")  #
ORDER_DB_PORT = os.getenv("ORDER_DB_PORT")  #
ORDER_DB_NAME = os.getenv("ORDER_DB_NAME")  #
#############################################

