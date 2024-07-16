"""
plan_values app service and repository
"""

from uuid import UUID
from sqlalchemy.exc import IntegrityError

from src.exceptions import ConflictException, NotFoundException
from src.organization_types.schemas import OrganizationTypeCreateSchema
from src.abstract_repository import SQLAlchemyRepository, AbstractRepository
from src.organization_types.models import OrganizationType

# define your service here and rename if it's necessary
# WARNING: if this sevice doesn't work with DB,
# you may implement only your own service

class OrganizationTypeRepository(SQLAlchemyRepository):
    model = OrganizationType


class OrganizationTypeService:
    def __init__(self, repository: AbstractRepository):
        self.repo: AbstractRepository = repository()

    async def get_all(self, limit: int, offset: int):
        if organization_type := await self.repo.get_all(limit, offset):
            return organization_type
        raise NotFoundException()

    async def get_by_uuid(self, uuid: UUID):
        if organization_type := await self.repo.get_by_uuid(uuid):
            return organization_type
        raise NotFoundException()

    async def delete_by_uuid(self, uuid: UUID):
        if organization_type := await self.repo.delete_by_uuid(uuid):
            return organization_type
        raise NotFoundException()
        
    async def create(self, organization_type: OrganizationTypeCreateSchema):
        organization_type_dict = organization_type.model_dump()
        try:
            new_organization_type = await self.repo.add(organization_type_dict)
            return new_organization_type
        except IntegrityError:
            raise ConflictException()