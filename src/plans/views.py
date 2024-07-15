"""
Views controllers for plans app
"""


from uuid import UUID
from fastapi import APIRouter, Depends, status, HTTPException

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


router = APIRouter(
    prefix=PREFIX,
    tags=TAGS,
    include_in_schema=INCLUDE_IN_SCHEMA
)


@router.get('/', response_model=PlanGetSchema, status_code=status.HTTP_200_OK)
async def get_one(
   uuid: UUID,
   plan_service: PlanService = Depends(get_plan_service)
):
    if plan := await plan_service.get_by_uuid(uuid):
        return plan
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.post('/', response_model=PlanGetSchema, status_code=status.HTTP_201_CREATED)
async def create_one(
    plan: PlanCreateSchema,
    plan_service: PlanService = Depends(get_plan_service)
):
    plan = await plan_service.add(plan)
    return plan


@router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_one(
    uuid: UUID,
    plan_service: PlanService = Depends(get_plan_service)
):
    await plan_service.delete_by_uuid(uuid)
    

@router.get('/all', status_code=status.HTTP_200_OK)
async def get_all(
    limit: int = 10,
    offset: int = 0,
    plan_service: PlanService = Depends(get_plan_service)
):
    plans = await plan_service.get_all()
    return plans[offset:offset+limit]
    