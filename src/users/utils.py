"""
Utils functions for users app
"""
import time
from fastapi.security import OAuth2PasswordBearer
import jwt
import hashlib

from src.auth.config import JWT_SECRET, JWT_ALGORITHM, EXPIRATION_TIME


# JWT

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def sign_jwt(user_id: int) -> dict:
    payload = {
        "user_id": str(user_id),
        "exp": time.time() + EXPIRATION_TIME
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def decode_jwt(token: str) -> dict:
    decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    return decoded_token if decoded_token.get('exp') >= time.time() else None

    
def my_hash(value: str) -> str:
    return hashlib.md5(value.encode('utf-8')).hexdigest()