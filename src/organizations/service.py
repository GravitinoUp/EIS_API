"""
plan_values app service and repository
"""

from uuid import UUID
from sqlalchemy.exc import IntegrityError

from src.exceptions import ConflictException, NotFoundException
from src.organizations.schemas import OrganizationCreateSchema
from src.abstract_repository import SQLAlchemyRepository, AbstractRepository
from src.organizations.models import Organization

# define your service here and rename if it's necessary
# WARNING: if this sevice doesn't work with DB,
# you may implement only your own service

class OrganizationRepository(SQLAlchemyRepository):
    model = Organization


class OrganizationService:
    def __init__(self, repository: AbstractRepository):
        self.repo: AbstractRepository = repository()

    async def get_all(self, limit: int, offset: int):
        if organization := await self.repo.get_all(limit, offset):
            return organization
        raise NotFoundException()

    async def get_by_uuid(self, uuid: UUID):
        if organization := await self.repo.get_by_uuid(uuid):
            return organization
        raise NotFoundException()

    async def delete_by_uuid(self, uuid: UUID):
        if organization := await self.repo.delete_by_uuid(uuid):
            return organization
        raise NotFoundException()
        
    async def create(self, organization: OrganizationCreateSchema):
        organization_dict = organization.model_dump()
        try:
            new_organization = await self.repo.add(organization_dict)
            return new_organization
        except IntegrityError:
            raise ConflictException()