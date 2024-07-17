from uuid import UUID
from sqlalchemy.exc import IntegrityError
from typing import Dict, List

from src.abstract_repository import SQLAlchemyRepository, AbstractRepository
from src.exceptions import ConflictException, NotFoundException
from src.plans.models import Plan, Purchase, PlanPurchase
from src.plans.schemas import PlanCreateSchema, PlanGetSchema, PurchaseGetSchema, PlanBaseSchema


class PlanRepository(SQLAlchemyRepository):
    model = Plan


class PurchaseRepository(SQLAlchemyRepository):
    model = Purchase


class PlanPurchaseRepository(SQLAlchemyRepository):
    model = PlanPurchase


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
                purchases.append(PurchaseGetSchema.model_validate(new_purchase, from_attributes=True))

            new_plan_schema = PlanGetSchema(
                **new_plan.__dict__,
                purchases=purchases
            )
            return new_plan_schema
        except IntegrityError:
            raise ConflictException()

    async def get_by_uuid(self, uuid: UUID) -> PlanGetSchema:
        if plan := await self.plan_repo.get_by_uuid(uuid):
            raise NotFoundException()

        purchases = await self._get_purchases_for_plan(plan.uuid)
        plan_schema = PlanGetSchema(
            **plan.__dict__,
            purchases=purchases
        )
        return plan_schema

    async def delete_by_uuid(self, uuid: UUID):
        if not await self.plan_repo.delete_by_uuid(uuid):
            raise NotFoundException()

    async def get_all(self, limit: int, offset: int) -> List[PlanGetSchema]:
        if plans := await self.plan_repo.get_all(limit, offset):
            print('plan not found')
            raise NotFoundException()

        plan_schemas = []
        for plan in plans:
            purchases = await self._get_purchases_for_plan(plan.uuid)
            plan_schema = PlanGetSchema(
                **plan.__dict__,
                purchases=purchases
            )
            plan_schemas.append(plan_schema)
        return plan_schemas

    async def _get_purchases_for_plan(self, plan_uuid: UUID) -> List[PurchaseGetSchema]:
        plan_purchases = await self.plan_purchase_repo.get_by_uuid(plan_uuid)
        purchases = []
        for plan_purchase in plan_purchases:
            purchase = await self.purchase_repo.get_by_uuid(plan_purchase.purchase_uuid)
            purchases.append(PurchaseGetSchema.model_validate(purchase, from_attributes=True))
        return purchases
