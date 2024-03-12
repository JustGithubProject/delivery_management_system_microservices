import os

from dotenv import load_dotenv


env_file_path = '.env_db'

load_dotenv(dotenv_path=env_file_path)

###########################################
AUTH_DB_USER = os.getenv("AUTH_DB_USER")  #
AUTH_DB_PASS = os.getenv("AUTH_DB_PASS")  #
AUTH_DB_NAME = os.getenv("AUTH_DB_NAME")  #
AUTH_DB_PORT = os.getenv("AUTH_DB_PORT")  #
AUTH_DB_HOST = os.getenv("AUTH_DB_HOST")  #
###########################################

env_file_path = '.env'

load_dotenv(dotenv_path=env_file_path)

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')   # should be kept secret
JWT_REFRESH_SECRET_KEY = os.getenv('JWT_REFRESH_SECRET_KEY')   # should be kept secret
