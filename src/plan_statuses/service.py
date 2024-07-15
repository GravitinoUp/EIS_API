"""
plan_statuses app service and repository
"""

from typing import List
from fastapi import HTTPException

from src.abstract_repository import SQLAlchemyRepository, AbstractRepository
from src.plan_statuses.models import PlanStatus
from src.plan_statuses.schemas import PlanStatusCreateSchema


# define your service here and rename if it's necessary
# WARNING: if this sevice doesn't work with DB,
# you may implement only your own service


class PlanStatusRepository(SQLAlchemyRepository):
    model = PlanStatus


class PlanStatusService:
    def __init__(self, repository: AbstractRepository):
        self.repo: AbstractRepository = repository()

    async def add(self, plan_status: PlanStatusCreateSchema):
        plan_status_dict = plan_status.model_dump()
        try:
            new_plan_status: PlanStatus = await self.repo.add(plan_status_dict)
            return new_plan_status
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=f"couldn't create plan_status: {e}",
            )
    
    async def get_by_id(self, id: int):
        plan_status: PlanStatus = await self.repo.get_by_id(id)
        return plan_status
    
    async def delete_by_id(self, id: int):
        plan_status: PlanStatus = await self.repo.delete_by_id(id)
        return plan_status
    
    async def get_all(self):
        plan_statuses: List[PlanStatus] = await self.repo.get_all()
        return plan_statuses
    