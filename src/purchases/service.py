"""
purchases app service and repository
"""

from uuid import UUID
from sqlalchemy.exc import IntegrityError

from src.abstract_repository import SQLAlchemyRepository, AbstractRepository
from src.purchases.models import Purchase
from src.exceptions import ConflictException, NotFoundException
from src.purchases.schemas import PurchaseCreateSchema


class PurchaseRepository(SQLAlchemyRepository):
    model = Purchase


class PurchaseService:
    def __init__(self, repository: AbstractRepository):
        self.repository: AbstractRepository = repository()

    async def get_by_uuid(self, uuid: UUID):
        if purchase := await self.repository.get_by_uuid(uuid):
            return purchase
        raise NotFoundException()

    async def get_all(self, limit: int, offset: int):
        if items := await self.repository.get_all(limit, offset):
            return items
        raise NotFoundException()
    
    async def get_status_by_data(self, purchase: PurchaseCreateSchema):
        item_dict = purchase.model_dump()   
        if item := await self.repository.get_by_data(**item_dict):
            return item.status
        raise NotFoundException()

    async def delete(self, uuid: UUID):
        if item := await self.repository.delete_by_uuid(uuid):
            return item
        raise NotFoundException()