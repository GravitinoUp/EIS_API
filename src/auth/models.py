"""
Database models of users app
"""

# you need to import Base from [project_name].database
from src.database import Base
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    role_id = Column(Integer, ForeignKey('role.id'), nullable=False)
    hashed_password: str = Column(String(50), nullable=False)
    email: str = Column(String(30), unique=True, nullable=False)
    username: str = Column(String(30), unique=True, nullable=False)
    phone_number = Column(String(20), unique=True, nullable=False)
    full_name = Column(String)

    role = relationship("Role", backref="user")


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)