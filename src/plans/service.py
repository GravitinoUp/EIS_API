from uuid import UUID
from sqlalchemy.exc import IntegrityError
from sqlalchemy import delete, select, update
from typing import List
import time
import asyncio

from src.abstract_repository import SQLAlchemyRepository
from src.exceptions import ConflictException, NotFoundException
from src.plans.models import Plan, PlanPurchase
from src.purchases.models import Purchase
from src.plans.schemas import PlanCreateSchema, PlanGetSchema, PurchaseGetSchema
from src.database import async_session_maker
from src.purchases.service import PurchaseRepository


class PlanRepository(SQLAlchemyRepository):
    model = Plan
    
    async def update_status_by_uuid(self, uuid: UUID):
        await asyncio.sleep(30)
        async with async_session_maker() as session:
            stmt = update(self.model).filter_by(uuid=uuid).values(
                status='Опубликован',
            )
            await session.execute(stmt)
            await session.commit()


class PlanPurchaseRepository(SQLAlchemyRepository):
    model = PlanPurchase

    async def get_all(self, plan_uuid: UUID):
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(plan_uuid=plan_uuid)
            res = await session.execute(statement=stmt)
            return res.scalars().all()
        
    async def delete_by_uuid(self, uuid: UUID):
        async with async_session_maker() as session:
            stmt = delete(self.model).filter_by(plan_uuid=uuid).returning(self.model)
            res = await session.execute(statement=stmt)
            await session.commit()
            return res.scalar()
        
    
class PlanService:
    def __init__(self, plan_repo: PlanRepository, purchase_repo: PurchaseRepository, plan_purchase_repo: PlanPurchaseRepository):
        self.plan_repo = plan_repo
        self.purchase_repo = purchase_repo
        self.plan_purchase_repo = plan_purchase_repo

    async def create(self, plan: PlanCreateSchema) -> PlanGetSchema:
        try:
            new_plan = await self.plan_repo.add(plan.model_dump(exclude={'purchases'}))

            purchases = []
            for purchase_data in plan.purchases:
                new_purchase = await self.purchase_repo.add(purchase_data.model_dump())
                await self.plan_purchase_repo.add({
                    "plan_uuid": new_plan.uuid,
                    "purchase_uuid": new_purchase.uuid
                })
                asyncio.create_task(self.purchase_repo.update_status_by_uuid(uuid=new_purchase.uuid)) # add background task
                purchases.append(PurchaseGetSchema.model_validate(new_purchase, from_attributes=True))

            new_plan_schema = PlanGetSchema(
                **new_plan.__dict__,
                purchases=purchases
            )
            
            asyncio.create_task(self.plan_repo.update_status_by_uuid(uuid=new_plan.uuid)) # add background task
            
            return new_plan_schema
        except IntegrityError as e:
            print(e)
            raise ConflictException()

    async def get_by_uuid(self, uuid: UUID) -> PlanGetSchema:
        plan = await self.plan_repo.get_by_uuid(uuid)
        if plan is None:
            raise NotFoundException()

        purchases = await self._get_purchases_for_plan(plan.uuid)
        plan_schema = PlanGetSchema(
            **plan.__dict__,
            purchases=purchases
        )
        return plan_schema

    async def delete_by_uuid(self, uuid: UUID):
        plan = await self.plan_repo.delete_by_uuid(uuid)
        if plan is None:
            raise NotFoundException()
        purchases = await self._get_purchases_for_plan(plan.uuid)
        for purchase in purchases:
            await self.purchase_repo.delete_by_uuid(purchase.uuid)
            await self.plan_purchase_repo.delete_by_uuid(plan.uuid)
        
    async def get_all(self, limit: int, offset: int) -> List[PlanGetSchema]:
        plans = await self.plan_repo.get_all(limit, offset)
        if plans is None:
            raise NotFoundException()
        plan_schemas = []
        for plan in plans:
            purchases = await self._get_purchases_for_plan(plan.uuid)
            plan_schema = PlanGetSchema(
                **plan.__dict__,
                purchases=purchases
            )
            plan_schemas.append(plan_schema)
        if not plan_schemas:
            raise NotFoundException()
        return plan_schemas

    async def _get_purchases_for_plan(self, plan_uuid: UUID) -> List[PurchaseGetSchema]:
        plan_purchases = await self.plan_purchase_repo.get_all(plan_uuid=plan_uuid)
        purchases = []
        for plan_purchase in plan_purchases:
            purchase = await self.purchase_repo.get_by_uuid(plan_purchase.purchase_uuid)
            if purchase is not None:
                purchases.append(PurchaseGetSchema.model_validate(purchase, from_attributes=True))
        return purchases
