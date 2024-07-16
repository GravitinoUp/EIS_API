"""
purchases app service and repository
"""

from uuid import UUID
from sqlalchemy.exc import IntegrityError

from exceptions import ConflictException, NotFoundException
from src.abstract_repository import SQLAlchemyRepository, AbstractRepository
from src.purchases.models import Purchase
from src.purchases.schemas import PurchaseCreateSchema

class PurchaseRepository(SQLAlchemyRepository):
    model = Purchase


class PurchaseService:
    def __init__(self, repository: AbstractRepository):
        self.repo: AbstractRepository = repository()
        
    async def add(self, item: PurchaseCreateSchema):
        item_dict = item.model_dump()
        try:
            new_item = await self.repo.add(item_dict)
            return new_item
        except IntegrityError:
            raise ConflictException()
    
    async def get_by_uuid(self, uuid: UUID):
        if item := await self.repo.get_by_uuid(uuid):
            return item
        raise NotFoundException()
    
    async def delete_by_uuid(self, uuid: UUID):
        if item := await self.repo.delete_by_uuid(uuid):
            return item
        raise NotFoundException()
    
    async def get_all(self, limit: int, offset: int):
        if items := await self.repo.get_all(limit, offset):
            return items
        raise NotFoundException()
