"""
Utils functions for users app
"""
import time
from uuid import UUID
from fastapi.security import OAuth2PasswordBearer
import jwt
import hashlib

from src.users.config import JWT_SECRET, JWT_ALGORITHM, EXPIRATION_TIME


# JWT

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")


def sign_jwt(user_uuid: UUID) -> dict:
    payload = {
        "user_uuid": str(user_uuid),
        "exp": time.time() + EXPIRATION_TIME
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def decode_jwt(token: str) -> dict:
    decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    return decoded_token if decoded_token.get('exp') >= time.time() else None

    
def my_hash(value: str) -> str:
    return hashlib.md5(value.encode('utf-8')).hexdigest()