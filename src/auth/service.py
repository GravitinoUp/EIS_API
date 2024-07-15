"""
users app service and repository
"""

from typing import List
from fastapi import HTTPException

from src.auth.models import User
from src.auth.schemas import UserCreateSchema
from src.abstract_repository import SQLAlchemyRepository, AbstractRepository
from src.auth.utils import my_hash


class UserRepository(SQLAlchemyRepository):
    model = User


class UserService:
    def __init__(self, user_repo: AbstractRepository) -> None:
        self.users_repo: AbstractRepository = user_repo()

    async def add_user(self, user: UserCreateSchema):
        user_dict: dict = user.model_dump()
        user_dict['hashed_password'] = my_hash(user_dict['password'])
        user_dict.pop('password')
        try:
            new_user: User = await self.users_repo.add_one(user_dict)
            new_user.__delattr__('hashed_password')
            return new_user
        except Exception:
            raise HTTPException(
                status_code=400,
                detail=f"User with data {user} already exists",
            )
    
    async def get_one_by_id(self, id: int):
        user: User = await self.users_repo.get_one_by_id(id)
        return user
    
    async def get_one_by_data(self, username: str, password: str):
        user: User = await self.users_repo.get_one_by_data(username=username, hashed_password=my_hash(password))
        return user
    
    async def update_one(self, email: str, password: str, new_password: str):
        old_data: dict = {"email": email, "hashed_password": my_hash(password)}
        new_data: dict = {"hashed_password": my_hash(new_password)}
        user: User = await self.users_repo.update_one_by_data(old_data, new_data)
        return user 
    
    async def delete_by_id(self, id: int):
        user: User = await self.users_repo.delete_one_by_id(id)
        return user
    
    async def get_all(self, limit: int = 10):
        users: List[User] = await self.users_repo.get_all(limit)
        return users