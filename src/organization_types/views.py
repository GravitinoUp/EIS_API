"""
Views controllers for plan_values app
"""


from uuid import UUID
from fastapi import APIRouter, Depends, status

from src.organization_types.service import OrganizationTypeService
from src.organization_types.dependencies import get_organization_type_service
from src.organization_types.schemas import OrganizationTypeCreateSchema, OrganizationTypeGetSchema
from src.users.utils import oauth2_scheme
from src.organization_types.config import (
    PREFIX,
    TAGS,
    INCLUDE_IN_SCHEMA
)


router = APIRouter(
    prefix=PREFIX,
    tags=TAGS,
    include_in_schema=INCLUDE_IN_SCHEMA,
    dependencies=[Depends(oauth2_scheme)],

)


@router.get('/', response_model=OrganizationTypeGetSchema, status_code=status.HTTP_200_OK)
async def get_one(
    uuid: UUID,
    service: OrganizationTypeService = Depends(get_organization_type_service)
):
    organization_type = await service.get_by_uuid(uuid)
    return organization_type


@router.post('/', response_model=OrganizationTypeGetSchema, status_code=status.HTTP_201_CREATED)
async def create_one(
    organization_type: OrganizationTypeCreateSchema,
    service: OrganizationTypeService = Depends(get_organization_type_service)
):
    new_organization_type = await service.create(organization_type)
    return new_organization_type


@router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_one(
    uuid: UUID,
    service: OrganizationTypeService = Depends(get_organization_type_service)
):
    await service.delete_by_uuid(uuid)


@router.get('/all', status_code=status.HTTP_200_OK)
async def get_all(
    limit: int = 10,
    offset: int = 0,
    service: OrganizationTypeService = Depends(get_organization_type_service)
):
    organization_type = await service.get_all(limit, offset)
    return organization_type