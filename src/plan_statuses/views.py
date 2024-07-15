"""
Views controllers for plan_statuses app
"""


from fastapi import APIRouter, Depends, HTTPException, status

from src.plan_statuses.config import (
    PREFIX,
    TAGS,
    INCLUDE_IN_SCHEMA
)
from src.plan_statuses.dependencies import get_plan_status_service
from src.plan_statuses.schemas import PlanStatusCreateSchema, PlanStatusGetSchema
from src.plan_statuses.service import PlanStatusService


router = APIRouter(
    prefix=PREFIX,
    tags=TAGS,
    include_in_schema=INCLUDE_IN_SCHEMA
)


@router.get('/', response_model=PlanStatusGetSchema, status_code=status.HTTP_200_OK)
async def get_one(
   id: str,
   plan_status_service: PlanStatusService = Depends(get_plan_status_service)
):
    if plan_stauts := await plan_status_service.get_by_id(id):
        return plan_stauts
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.post('/', response_model=PlanStatusGetSchema, status_code=status.HTTP_201_CREATED)
async def create_one(
    plan_status: PlanStatusCreateSchema,
    plan_status_service: PlanStatusService = Depends(get_plan_status_service)
):
    plan_status = await plan_status_service.add(plan_status)
    return plan_status


@router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_one(
    id: str,
    plan_status_service: PlanStatusService = Depends(get_plan_status_service)
):
    await plan_status_service.delete_by_id(id)
    

@router.get('/all', status_code=status.HTTP_200_OK)
async def get_all(
    limit: int = 10,
    offset: int = 0,
    plan_status_service: PlanStatusService = Depends(get_plan_status_service)
):
    plan_statuses = await plan_status_service.get_all()
    return plan_statuses[offset:offset+limit]
    