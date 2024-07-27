"""
Views controllers for plans app
"""


from fastapi import APIRouter, Depends, status

from src.plans.config import (
    PREFIX,
    TAGS,
    INCLUDE_IN_SCHEMA
)
from src.plans.dependencies import get_plan_service
from src.plans.schemas import PlanCreateSchema, PlanGetSchema
from src.plans.service import PlanService
from src.users.utils import oauth2_scheme


router = APIRouter(
    prefix=PREFIX,
    tags=TAGS,
    include_in_schema=INCLUDE_IN_SCHEMA,
    # dependencies=[Depends(oauth2_scheme)]
)


@router.get('/{id}', response_model=PlanGetSchema, status_code=status.HTTP_200_OK)
async def get_one(
    id: int,
    service: PlanService = Depends(get_plan_service)
):
    """
    Получение плана-графика по id.
    """
    plan = await service.get_by_id(id)
    return plan


@router.post('/', response_model=PlanGetSchema, status_code=status.HTTP_201_CREATED)
async def create_one(
    plan: PlanCreateSchema,
    service: PlanService = Depends(get_plan_service)
):
    """
    Добавление плана-графика.
    """
    new_plan = await service.create(plan)
    return new_plan


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_one(
    id: int,
    service: PlanService = Depends(get_plan_service)
):
    """
    Удаление плана графика по id.
    """
    await service.delete_by_id(id)


@router.get('', status_code=status.HTTP_200_OK)
async def get_all(
    limit: int = 10,
    offset: int = 0,
    service: PlanService = Depends(get_plan_service)
):
    """
    Получение всех планов-графиков с лимитом (limit) и сдвигом (offset)
    """
    plans = await service.get_all(limit, offset)
    return plans