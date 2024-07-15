"""
plans app service and repository
"""

from typing import List
from uuid import UUID
from fastapi import HTTPException
from src.abstract_repository import SQLAlchemyRepository, AbstractRepository
from src.plans.models import Plan
from src.plans.schemas import PlanCreateSchema

# define your service here and rename if it's necessary
# WARNING: if this sevice doesn't work with DB,
# you may implement only your own service


class PlanRepository(SQLAlchemyRepository):
    model = Plan


class PlanService:
    def __init__(self, repository: AbstractRepository):
        self.repo: AbstractRepository = repository()

    async def add(self, plan: PlanCreateSchema):
        plan_dict = plan.model_dump()
        try:
            new_plan: Plan = await self.repo.add(plan_dict)
            return new_plan
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=f"couldn't create plan: {e}",
            )
    
    async def get_by_uuid(self, uuid: UUID):
        plan: Plan = await self.repo.get_by_uuid(uuid)
        return plan
    
    async def delete_by_uuid(self, uuid: UUID):
        plan: Plan = await self.repo.delete_by_uuid(uuid)
        return plan
    
    async def get_all(self):
        plans: List[Plan] = await self.repo.get_all()
        return plans
    