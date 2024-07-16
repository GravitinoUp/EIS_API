"""
currency app service and repository
"""

from sqlalchemy.exc import IntegrityError

from exceptions import ConflictException, NotFoundException
from src.abstract_repository import SQLAlchemyRepository, AbstractRepository
from src.currency.models import Currency
from src.currency.schemas import CurrencyCreateSchema


class CurrencyRepository(SQLAlchemyRepository):
    model = Currency


class CurrencyService:
    def __init__(self, repository: AbstractRepository):
        self.repo: AbstractRepository = repository()
        
    async def add(self, item: CurrencyCreateSchema):
        item_dict = item.model_dump()
        try:
            new_item = await self.repo.add(item_dict)
            return new_item
        except IntegrityError:
            raise ConflictException()
    
    async def get_by_id(self, id: int):
        if item := await self.repo.get_by_id(id):
            return item
        raise NotFoundException()
    
    async def delete_by_id(self, id: int):
        if item := await self.repo.delete_by_id(id):
            return item
        raise NotFoundException()
    
    async def get_all(self, limit: int, offset: int):
        if items := await self.repo.get_all(limit, offset):
            return items
        raise NotFoundException()