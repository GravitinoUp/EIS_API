"""
tech_tasks app service and repository
"""
from uuid import UUID
from sqlalchemy.exc import IntegrityError

from src.exceptions import ConflictException, NotFoundException
from src.abstract_repository import SQLAlchemyRepository, AbstractRepository
from src.tech_tasks.models import TechTask
from src.tech_tasks.schemas import TechTaskCreateSchema


# define your service here and rename if it's necessary
# WARNING: if this sevice doesn't work with DB,
# you may implement only your own service

class TechTaskRepository(SQLAlchemyRepository):
    model = TechTask


class TechTaskService:
    def __init__(self, repository: AbstractRepository):
        self.repo: AbstractRepository = repository()

    async def get_all(self, limit: int, offset: int):
        if tech_task := await self.repo.get_all(limit, offset):
            return tech_task
        raise NotFoundException()

    async def get_by_uuid(self, uuid: UUID):
        if tech_task := await self.repo.get_by_uuid(uuid):
            return tech_task
        raise NotFoundException()

    async def delete_by_uuid(self, uuid: UUID):
        if tech_task := await self.repo.delete_by_uuid(uuid):
            return tech_task
        raise NotFoundException()
        
    async def create(self, tech_task: TechTaskCreateSchema):
        tech_task_dict = tech_task.model_dump()
        try:
            new_tech_task = await self.repo.add(tech_task_dict)
            return new_tech_task
        except IntegrityError:
            raise ConflictException()