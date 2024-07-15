"""
Views controllers for plans app
"""

from uuid import UUID
from fastapi import APIRouter, Depends, status

from src.plans.config import (
    PREFIX,
    TAGS,
    INCLUDE_IN_SCHEMA
)
from src.plans.schemas import (
    PlanCreateSchema, PlanGetSchema,
)
from src.plans.dependencies import get_plan_service
from src.plans.service import PlanService
from src.auth.utils import oauth2_scheme


router = APIRouter(
    prefix=PREFIX,
    tags=TAGS,
    include_in_schema=INCLUDE_IN_SCHEMA,
    dependencies=[Depends(oauth2_scheme)]
)


@router.get('/', response_model=PlanGetSchema, status_code=status.HTTP_200_OK)
async def get_one(
    uuid: UUID,
    service: PlanService = Depends(get_plan_service)
):
    plan = await service.get_by_uuid(uuid)
    return plan


@router.post('/', response_model=PlanGetSchema, status_code=status.HTTP_201_CREATED)
async def create_one(
    plan: PlanCreateSchema,
    service: PlanService = Depends(get_plan_service)
):
    plan = await service.add(plan)
    return plan


@router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_one(
    uuid: UUID,
    service: PlanService = Depends(get_plan_service)
):
    await service.delete_by_uuid(uuid)
    

@router.get('/all', status_code=status.HTTP_200_OK)
async def get_all(
    limit: int = 10,
    offset: int = 0,
    service: PlanService = Depends(get_plan_service)
):
    plans = await service.get_all(limit, offset)
    return plans
    