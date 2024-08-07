from sqlalchemy.exc import IntegrityError
from typing import List

from src.exceptions import ConflictException, NotFoundException
from src.plans.schemas import PlanCreateSchema, PlanGetSchema, PurchaseGetSchema
from src.purchases.service import PurchaseRepository
from src.plans.repositories import PlanRepository, PlanPurchaseRepository
        
    
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
                new_purchase = await self.purchase_repo.add(purchase_data.custom_dict())
                await self.plan_purchase_repo.add({
                    "plan_id": new_plan.id,
                    "purchase_id": new_purchase.id
                })
                purchases.append(PurchaseGetSchema.from_model(new_purchase))

            new_plan_schema = PlanGetSchema(
                **new_plan.__dict__,
                purchases=purchases
            )
            
            
            return new_plan_schema
        except IntegrityError:
            raise ConflictException()

    async def get_by_id(self, id: int) -> PlanGetSchema:
        plan = await self.plan_repo.get_by_id(id)
        if plan is None:
            raise NotFoundException()

        purchases = await self._get_purchases_for_plan(plan.id)
        plan_schema = PlanGetSchema(
            **plan.__dict__,
            purchases=purchases
        )
        return plan_schema

    async def delete_by_id(self, id: int):
        plan = await self.plan_repo.delete_by_id(id)
        if plan is None:
            raise NotFoundException()
        purchases = await self._get_purchases_for_plan(plan.id)
        for purchase in purchases:
            await self.purchase_repo.delete_by_id(purchase.id)
            await self.plan_purchase_repo.delete_by_id(plan.id)
        
    async def get_all(self, limit: int, offset: int) -> List[PlanGetSchema]:
        plans = await self.plan_repo.get_all(limit, offset)
        if plans is None:
            raise NotFoundException()
        plan_schemas = []
        for plan in plans:
            purchases = await self._get_purchases_for_plan(plan.id)
            plan_schema = PlanGetSchema(
                **plan.__dict__,
                purchases=purchases
            )
            plan_schemas.append(plan_schema)
        if not plan_schemas:
            raise NotFoundException()
        return plan_schemas

    async def _get_purchases_for_plan(self, plan_id: int) -> List[PurchaseGetSchema]:
        plan_purchases = await self.plan_purchase_repo.get_all(plan_id=plan_id)
        purchases = []
        for plan_purchase in plan_purchases:
            purchase = await self.purchase_repo.get_by_id(plan_purchase.purchase_id)
            if purchase is not None:
                purchases.append(PurchaseGetSchema.from_model(purchase))
        return purchases
