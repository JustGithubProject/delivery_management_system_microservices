import os

from dotenv import load_dotenv


env_file_path = '.env'

load_dotenv(dotenv_path=env_file_path)

###############################################################
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")                  #
JWT_REFRESH_SECRET_KEY = os.getenv("JWT_REFRESH_SECRET_KEY")  #
###############################################################

