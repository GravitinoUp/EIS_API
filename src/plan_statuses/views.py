"""
Views controllers for plan_statuses app
"""


from fastapi import APIRouter, Depends, status

from src.plan_statuses.config import (
    PREFIX,
    TAGS,
    INCLUDE_IN_SCHEMA
)
from src.plan_statuses.dependencies import get_plan_status_service
from src.plan_statuses.schemas import PlanStatusCreateSchema, PlanStatusGetSchema
from src.plan_statuses.service import PlanStatusService
from src.auth.utils import oauth2_scheme


router = APIRouter(
    prefix=PREFIX,
    tags=TAGS,
    include_in_schema=INCLUDE_IN_SCHEMA,
    dependencies=[Depends(oauth2_scheme)]
)


@router.get('/', response_model=PlanStatusGetSchema, status_code=status.HTTP_200_OK)
async def get_one(
   id: int,
   service: PlanStatusService = Depends(get_plan_status_service)
):
    plan_stauts = await service.get_by_id(id)
    return plan_stauts
     


@router.post('/', response_model=PlanStatusGetSchema, status_code=status.HTTP_201_CREATED)
async def create_one(
    plan_status: PlanStatusCreateSchema,
    service: PlanStatusService = Depends(get_plan_status_service)
):
    plan_status = await service.add(plan_status)
    return plan_status


@router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_one(
    id: int,
    service: PlanStatusService = Depends(get_plan_status_service)
):
    await service.delete_by_id(id)
    

@router.get('/all', status_code=status.HTTP_200_OK)
async def get_all(
    limit: int = 10,
    offset: int = 0,
    service: PlanStatusService = Depends(get_plan_status_service)
):
    plan_statuses = await service.get_all(limit, offset)
    return plan_statuses
    