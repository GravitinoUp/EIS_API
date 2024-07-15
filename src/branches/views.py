"""
Views controllers for branches app
"""


from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status

from src.exceptions import NotFoundException
from src.branches.config import (
    PREFIX,
    TAGS,
    INCLUDE_IN_SCHEMA
)
from src.branches.dependencies import get_branch_service
from src.branches.schemas import BranchCreateSchema, BranchGetSchema
from src.branches.service import BranchService
from src.auth.utils import oauth2_scheme


router = APIRouter(
    prefix=PREFIX,
    tags=TAGS,
    include_in_schema=INCLUDE_IN_SCHEMA,
    dependencies=[Depends(oauth2_scheme)]
)


@router.get('/', response_model=BranchGetSchema, status_code=status.HTTP_200_OK)
async def get_one(
   uuid: UUID,
   service: BranchService = Depends(get_branch_service)
):
    branch = await service.get_by_uuid(uuid)
    return branch


@router.post('/', response_model=BranchGetSchema, status_code=status.HTTP_201_CREATED)
async def create_one(
    branch: BranchCreateSchema,
    service: BranchService = Depends(get_branch_service)
):
    branch = await service.add(branch)
    return branch


@router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_one(
    uuid: UUID,
    service: BranchService = Depends(get_branch_service)
):
    await service.delete_by_uuid(uuid)
    

@router.get('/all', status_code=status.HTTP_200_OK)
async def get_all(
    limit: int = 10,
    offset: int = 0,
    service: BranchService = Depends(get_branch_service)
):
    branches = await service.get_all(limit, offset)
    return branches
    
