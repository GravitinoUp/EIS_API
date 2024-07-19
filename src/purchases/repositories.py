import asyncio
import random

from sqlalchemy import update
from src.abstract_repository import SQLAlchemyRepository
from src.purchases.models import Purchase
from src.database import async_session_maker


class PurchaseRepository(SQLAlchemyRepository):
    model = Purchase
    
    async def update_status_by_id(self, id: int):
        await asyncio.sleep(random.randint(30, 60))
        async with async_session_maker() as session:
            stmt = update(self.model).filter_by(id=id).values(
                status='Опубликован',
            )
            await session.execute(stmt)
            await session.commit()
        