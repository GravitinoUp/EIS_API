"""
Settings for app users
"""
import os
from dotenv import load_dotenv

# APIRouter settings
PREFIX = '/auth'  
TAGS = ['Auth'] # capitalize this if you need it
INCLUDE_IN_SCHEMA = True 

# define your config here for app users

load_dotenv()

JWT_SECRET = os.getenv('JWT_SECRET')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')
EXPIRATION_TIME = int(os.getenv('EXPIRATION_TIME'))