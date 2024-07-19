"""
This module is used to manage and connect to the database.
"""

import random
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from src.settings import ASYNC_DATABASE_URL


class Base(DeclarativeBase):
    __table_args__ = {
        'extend_existing': True
    }


engine = create_async_engine(ASYNC_DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


def generate_unique_id():
    return random.randint(100000000, 9999999999)