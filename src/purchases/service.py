"""
purchases app service and repository
"""

import asyncio
from src.abstract_repository import AbstractRepository
from src.exceptions import ConflictException, NotFoundException
from src.purchases.schemas import PurchaseCreateSchema, PurchaseGetSchema
from src.plans.repositories import PlanPurchaseRepository, PlanRepository
from src.purchases.repositories import PurchaseRepository


class PurchaseService:
    def __init__(self, purchase_repo: PurchaseRepository, plan_purchase_repo: PlanPurchaseRepository, plan_repo: PlanRepository):
        self.purchase_repo: PurchaseRepository = purchase_repo()
        self.plan_purchase_repo: PlanPurchaseRepository = plan_purchase_repo()
        self.plan_repo: PlanRepository = plan_repo()
        
    async def add(self, purhcase: PurchaseCreateSchema, plan_id: int):
        if purchase := await self.purchase_repo.add(purhcase.custom_dict()):
            if await self.plan_purchase_repo.add({"plan_id": plan_id, "purchase_id": purchase.id}):
                await self.plan_repo.update_version_by_id(plan_id)
                return PurchaseGetSchema.from_model(purchase)
        raise ConflictException()
    
    async def update_status(self, id: int):
        asyncio.create_task(self.purchase_repo.update_status_by_id(id=id))

    async def get_by_id(self, id: int):
        if purchase := await self.purchase_repo.get_by_id(id):
            return PurchaseGetSchema.from_model(purchase)
        raise NotFoundException()

    async def get_all(self, limit: int, offset: int):
        if items := await self.purchase_repo.get_all(limit, offset):
            return [PurchaseGetSchema.from_model(item) for item in items]
        raise NotFoundException()
    
    async def get_status_by_id(self, id: int):   
        if item := await self.purchase_repo.get_by_id(id):
            return item.status
        raise NotFoundException()

    async def delete(self, id: int):
        if item := await self.purchase_repo.delete_by_id(id):
            if await self.plan_purchase_repo.delete_by_purchase_id(item.id):
                return item
        raise NotFoundException()
    