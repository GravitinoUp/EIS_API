import asyncio
import random

from sqlalchemy import delete, select, update
from src.abstract_repository import SQLAlchemyRepository
from src.plans.models import Plan, PlanPurchase
from src.database import async_session_maker


class PlanRepository(SQLAlchemyRepository):
    model = Plan
    
    async def update_status_by_id(self, id: int):
        await asyncio.sleep(random.randint(120, 300))
        async with async_session_maker() as session:
            stmt = update(self.model).filter_by(id=id).values(
                status='Опубликован',
            )
            await session.execute(stmt)
            await session.commit()
            
    async def update_version_by_id(self, id: int):
        async with async_session_maker() as session:
            stmt = select(self.model).where(id==id)
            res = await session.execute(stmt)
            res = res.scalar()
            res.version = res.version + 1
            await session.commit()


class PlanPurchaseRepository(SQLAlchemyRepository):
    model = PlanPurchase

    async def get_all(self, plan_id: int):
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(plan_id=plan_id)
            res = await session.execute(statement=stmt)
            return res.scalars().all()
        
    async def delete_by_id(self, id: int):
        async with async_session_maker() as session:
            stmt = delete(self.model).filter_by(plan_id=id).returning(self.model)
            res = await session.execute(statement=stmt)
            await session.commit()
            return res.scalar()
        
    async def delete_by_purchase_id(self, id: int):
        async with async_session_maker() as session:
            stmt = delete(self.model).filter_by(purchase_id=id).returning(self.model)
            res = await session.execute(statement=stmt)
            await session.commit()
            return res.scalar()