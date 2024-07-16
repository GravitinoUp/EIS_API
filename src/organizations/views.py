"""
Views controllers for tech_tasks app
"""


from uuid import UUID
from fastapi import APIRouter, Depends, status

from src.tech_tasks.config import (
    PREFIX,
    TAGS,
    INCLUDE_IN_SCHEMA
)
from src.organizations.schemas import OrganizationCreateSchema, OrganizationGetSchema
from src.auth.utils import oauth2_scheme
from src.organizations.dependencies import get_organization_service
from src.organizations.service import OrganizationService


router = APIRouter(
    prefix=PREFIX,
    tags=TAGS,
    include_in_schema=INCLUDE_IN_SCHEMA,
    dependencies=[Depends(oauth2_scheme)],

)


@router.get('/', response_model=OrganizationGetSchema, status_code=status.HTTP_200_OK)
async def get_one(
    uuid: UUID,
    service: OrganizationService = Depends(get_organization_service)
):
    organization = await service.get_by_uuid(uuid)
    return organization


@router.post('/', response_model=OrganizationGetSchema, status_code=status.HTTP_201_CREATED)
async def create_one(
    organization: OrganizationCreateSchema,
    service: OrganizationService = Depends(get_organization_service)
):
    new_organization = await service.create(organization)
    return new_organization


@router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_one(
    uuid: UUID,
    service: OrganizationService = Depends(get_organization_service)
):
    await service.delete_by_uuid(uuid)


@router.get('/all', status_code=status.HTTP_200_OK)
async def get_all(
    limit: int = 10,
    offset: int = 0,
    service: OrganizationService = Depends(get_organization_service)
):
    organizations = await service.get_all(limit, offset)
    return organizations