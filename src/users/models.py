from uuid import uuid4
from src.database import Base
from sqlalchemy import UUID, Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'

    uuid = Column(UUID, primary_key=True, default=uuid4)
    role_id = Column(Integer, ForeignKey('role.id'), nullable=False)
    hashed_password = Column(String(50), nullable=False)
    email = Column(String(30), unique=True, nullable=False)
    username = Column(String(30), unique=True, nullable=False)
    phone_number = Column(String(20), unique=True, nullable=False)
    full_name = Column(String)
    
    role = relationship("Role", foreign_keys=[role_id])
    

class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
