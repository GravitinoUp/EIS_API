"""
plans app service and repository
"""

from typing import List
from uuid import UUID
from sqlalchemy.exc import IntegrityError
from src.exceptions import ConflictException, NotFoundException
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
        except IntegrityError:
            raise ConflictException()
    
    async def get_by_uuid(self, uuid: UUID):
        if plan := await self.repo.get_by_uuid(uuid):
            return plan
        raise NotFoundException()
    
    async def delete_by_uuid(self, uuid: UUID):
        if plan := await self.repo.delete_by_uuid(uuid):
            return plan
        raise NotFoundException()
    
    async def get_all(self, limit: int, offset: int):
        if plans := await self.repo.get_all(limit, offset):
            return plans
        raise NotFoundException()
    