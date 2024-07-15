"""
branches app service and repository
"""

from typing import List
from uuid import UUID
from fastapi import HTTPException

from src.abstract_repository import SQLAlchemyRepository, AbstractRepository
from src.branches.models import Branch
from src.branches.schemas import BranchCreateSchema


# define your service here and rename if it's necessary
# WARNING: if this sevice doesn't work with DB,
# you may implement only your own service

    
class BranchRepository(SQLAlchemyRepository):
    model = Branch


class BranchService:
    def __init__(self, repository: AbstractRepository):
        self.repo: AbstractRepository = repository()

    async def add(self, branch: BranchCreateSchema):
        branch_dict = branch.model_dump()
        try:
            new_branch: Branch = await self.repo.add(branch_dict)
            return new_branch
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=f"couldn't create branch: {e}",
            )
    
    async def get_by_uuid(self, uuid: UUID):
        branch: Branch = await self.repo.get_by_uuid(uuid)
        return branch
    
    async def delete_by_uuid(self, uuid: UUID):
        branch: Branch = await self.repo.delete_by_uuid(uuid)
        return branch
    
    async def get_all(self):
        branches: List[Branch] = await self.repo.get_all()
        return branches