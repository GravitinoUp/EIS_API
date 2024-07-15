"""
Views controllers for branches app
"""


from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status

from src.branches.config import (
    PREFIX,
    TAGS,
    INCLUDE_IN_SCHEMA
)
from src.branches.dependencies import get_branch_service
from src.branches.schemas import BranchCreateSchema, BranchGetSchema
from src.branches.service import BranchService


router = APIRouter(
    prefix=PREFIX,
    tags=TAGS,
    include_in_schema=INCLUDE_IN_SCHEMA
)


@router.get('/', response_model=BranchGetSchema, status_code=status.HTTP_200_OK)
async def get_one(
   uuid: UUID,
   branch_service: BranchService = Depends(get_branch_service)
):
    if branch := await branch_service.get_by_uuid(uuid):
        return branch
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.post('/', response_model=BranchGetSchema, status_code=status.HTTP_201_CREATED)
async def create_one(
    branch: BranchCreateSchema,
    branch_service: BranchService = Depends(get_branch_service)
):
    branch = await branch_service.add(branch)
    return branch


@router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_one(
    uuid: UUID,
    branch_service: BranchService = Depends(get_branch_service)
):
    await branch_service.delete_by_uuid(uuid)
    

@router.get('/all', status_code=status.HTTP_200_OK)
async def get_all(
    limit: int = 10,
    offset: int = 0,
    branch_service: BranchService = Depends(get_branch_service)
):
    branches = await branch_service.get_all()
    return branches[offset:offset+limit]
    
