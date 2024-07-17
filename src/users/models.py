from uuid import uuid4
from src.database import Base
from sqlalchemy import UUID, Column, String


class User(Base):
    __tablename__ = 'users'

    uuid = Column(UUID, primary_key=True, default=uuid4)
    hashed_password = Column(String(50), nullable=False)
    email = Column(String(30), unique=True, nullable=False)
    username = Column(String(30), unique=True, nullable=False)
