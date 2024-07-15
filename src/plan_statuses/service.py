"""
plan_statuses app service and repository
"""

from sqlalchemy.exc import IntegrityError

from src.exceptions import ConflictException, NotFoundException
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
        except IntegrityError:
            raise ConflictException()
    
    async def get_by_id(self, id: int):
        if plan_status := await self.repo.get_by_id(id):
            return plan_status
        raise NotFoundException()
    
    async def delete_by_id(self, id: int):
        if plan_status := await self.repo.delete_by_id(id):
            return plan_status
        raise NotFoundException()
    
    async def get_all(self, limit: int, offset: int):
        if plan_statuses := await self.repo.get_all(limit, offset):
            return plan_statuses
        raise NotFoundException()
    