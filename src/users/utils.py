"""
Utils functions for users app
"""
import hashlib
import time
from functools import wraps
from typing import Callable
from uuid import UUID

import jwt
from fastapi.security import OAuth2PasswordBearer

from src.users.config import EXPIRATION_TIME, JWT_ALGORITHM, JWT_SECRET


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