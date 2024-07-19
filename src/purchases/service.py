"""
purchases app service and repository
"""

import random
from uuid import UUID
from sqlalchemy import update
import asyncio

from src.abstract_repository import SQLAlchemyRepository, AbstractRepository
from src.purchases.models import Purchase
from src.exceptions import ConflictException, NotFoundException
from src.purchases.schemas import PurchaseCreateSchema, PurchaseGetSchema
from src.database import async_session_maker


class PurchaseRepository(SQLAlchemyRepository):
    model = Purchase
    
    async def update_status_by_id(self, id: int):
        await asyncio.sleep(random.randint(120, 300))
        async with async_session_maker() as session:
            stmt = update(self.model).filter_by(id=id).values(
                status='Опубликован',
            )
            await session.execute(stmt)
            await session.commit()
        

class PurchaseService:
    def __init__(self, repository: AbstractRepository):
        self.repository: AbstractRepository = repository()

    async def get_by_id(self, id: int):
        if purchase := await self.repository.get_by_id(id):
            return PurchaseGetSchema.from_model(purchase)
        raise NotFoundException()

    async def get_all(self, limit: int, offset: int):
        if items := await self.repository.get_all(limit, offset):
            return [PurchaseGetSchema.from_model(item) for item in items]
        raise NotFoundException()
    
    async def get_status_by_id(self, id: int):   
        if item := await self.repository.get_by_id(id):
            return item.status
        raise NotFoundException()

    async def delete(self, id: int):
        if item := await self.repository.delete_by_id(id):
            return item

        raise NotFoundException()
    
