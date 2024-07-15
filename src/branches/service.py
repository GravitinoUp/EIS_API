"""
branches app service and repository
"""


from uuid import UUID
from sqlalchemy.exc import IntegrityError

from src.exceptions import ConflictException, NotFoundException
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
        except IntegrityError:
            raise ConflictException()
    
    async def get_by_uuid(self, uuid: UUID):
        if branch := await self.repo.get_by_uuid(uuid):
            return branch
        raise NotFoundException()
    
    async def delete_by_uuid(self, uuid: UUID):
        if branch := await self.repo.delete_by_uuid(uuid):
            return branch
        raise NotFoundException()
    
    async def get_all(self, limit: int, offset: int):
        if branches := await self.repo.get_all(limit, offset):
            return branches
        raise NotFoundException()