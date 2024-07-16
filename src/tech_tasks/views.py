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
from src.tech_tasks.schemas import TechTaskCreateSchema, TechTaskGetSchema
from src.auth.utils import oauth2_scheme
from src.tech_tasks.dependencies import get_tech_task_service
from src.tech_tasks.service import TechTaskService


router = APIRouter(
    prefix=PREFIX,
    tags=TAGS,
    include_in_schema=INCLUDE_IN_SCHEMA,
    dependencies=[Depends(oauth2_scheme)],

)


@router.get('/', response_model=TechTaskGetSchema, status_code=status.HTTP_200_OK)
async def get_one(
    uuid: UUID,
    service: TechTaskService = Depends(get_tech_task_service)
):
    tech_task = await service.get_by_uuid(uuid)
    return tech_task


@router.post('/', response_model=TechTaskGetSchema, status_code=status.HTTP_201_CREATED)
async def create_one(
    plan_value: TechTaskCreateSchema,
    service: TechTaskService = Depends(get_tech_task_service)
):
    new_tech_task = await service.create(plan_value)
    return new_tech_task


@router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_one(
    uuid: UUID,
    service: TechTaskService = Depends(get_tech_task_service)
):
    await service.delete_by_uuid(uuid)


@router.get('/all', status_code=status.HTTP_200_OK)
async def get_all(
    limit: int = 10,
    offset: int = 0,
    service: TechTaskService = Depends(get_tech_task_service)
):
    tech_tasks = await service.get_all(limit, offset)
    return tech_tasks