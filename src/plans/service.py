"""
plans app service and repository
"""

from uuid import UUID
from sqlalchemy.exc import IntegrityError

from src.abstract_repository import SQLAlchemyRepository, AbstractRepository
from src.exceptions import ConflictException, NotFoundException
from src.plans.models import Plan
from src.plans.schemas import PlanCreateSchema


class PlanRepository(SQLAlchemyRepository):
    model = Plan


class PlanService:
    def __init__(self, repository: AbstractRepository):
        self.repository: AbstractRepository = repository()

    async def create(self, plan: PlanCreateSchema):
        plan_dict: dict = plan.model_dump()
        try:
            new_plan = await self.repository.add(plan_dict)
            return new_plan
        except IntegrityError:
            raise ConflictException()
    
    async def get_by_uuid(self, uuid: UUID):
        if plan := await self.repository.get_by_uuid(uuid):
            return plan
        raise NotFoundException()
    
    async def delete_by_uuid(self, uuid: UUID):
        if plan := await self.repository.delete_by_uuid(uuid):
            return plan
        raise NotFoundException()
    
    async def get_all(self, limit: int, offset: int):
        if plans := await self.repository.get_all(limit, offset):
            return plans
        raise NotFoundException()