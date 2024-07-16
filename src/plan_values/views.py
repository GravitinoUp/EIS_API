"""
Views controllers for plan_values app
"""


from uuid import UUID
from fastapi import APIRouter, Depends, status

from src.plan_values.service import PlanValueService
from src.plan_values.dependencies import get_plan_value_service
from src.plan_values.schemas import PlanValueCreateSchema, PlanValueGetSchema
from src.auth.utils import oauth2_scheme
from src.plan_values.config import (
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


@router.get('/', response_model=PlanValueGetSchema, status_code=status.HTTP_200_OK)
async def get_one(
    uuid: UUID,
    service: PlanValueService = Depends(get_plan_value_service)
):
    plan_value = await service.get_by_uuid(uuid)
    return plan_value


@router.post('/', response_model=PlanValueGetSchema, status_code=status.HTTP_201_CREATED)
async def create_one(
    plan_value: PlanValueCreateSchema,
    service: PlanValueService = Depends(get_plan_value_service)
):
    new_plan_value = await service.create(plan_value)
    return new_plan_value


@router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_one(
    uuid: UUID,
    service: PlanValueService = Depends(get_plan_value_service)
):
    await service.delete_by_uuid(uuid)


@router.get('/all', status_code=status.HTTP_200_OK)
async def get_all(
    limit: int = 10,
    offset: int = 0,
    service: PlanValueService = Depends(get_plan_value_service)
):
    plan_values = await service.get_all(limit, offset)
    return plan_values