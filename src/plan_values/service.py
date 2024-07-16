"""
plan_values app service and repository
"""

from uuid import UUID
from sqlalchemy.exc import IntegrityError

from src.exceptions import ConflictException, NotFoundException
from src.plan_values.schemas import PlanValueCreateSchema
from src.abstract_repository import SQLAlchemyRepository, AbstractRepository
from src.plan_values.models import PlanValue

# define your service here and rename if it's necessary
# WARNING: if this sevice doesn't work with DB,
# you may implement only your own service

class PlanValueRepository(SQLAlchemyRepository):
    model = PlanValue


class PlanValueService:
    def __init__(self, repository: AbstractRepository):
        self.repo: AbstractRepository = repository()

    async def get_all(self, limit: int, offset: int):
        if plan_values := await self.repo.get_all(limit, offset):
            return plan_values
        raise NotFoundException()

    async def get_by_uuid(self, uuid: UUID):
        if plan_value := await self.repo.get_by_uuid(uuid):
            return plan_value
        raise NotFoundException()

    async def delete_by_uuid(self, uuid: UUID):
        if plan_value := await self.repo.delete_by_uuid(uuid):
            return plan_value
        raise NotFoundException()
        
    async def create(self, plan_value: PlanValueCreateSchema):
        plan_value_dict = plan_value.model_dump()
        try:
            new_plan_value = await self.repo.add(plan_value_dict)
            return new_plan_value
        except IntegrityError:
            raise ConflictException()