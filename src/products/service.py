"""
products app service and repository
"""
from uuid import UUID
from sqlalchemy.exc import IntegrityError

from src.exceptions import ConflictException, NotFoundException
from src.abstract_repository import SQLAlchemyRepository, AbstractRepository
from src.products.models import Product
from src.products.schemas import ProductCreateSchema


# define your service here and rename if it's necessary
# WARNING: if this sevice doesn't work with DB,
# you may implement only your own service

class ProductRepository(SQLAlchemyRepository):
    model = Product


class ProductService:
    def __init__(self, repository: AbstractRepository):
        self.repo: AbstractRepository = repository()
        
    async def add(self, item: ProductCreateSchema):
        item_dict = item.model_dump()
        try:
            new_item = await self.repo.add(item_dict)
            return new_item
        except IntegrityError:
            raise ConflictException()
    
    async def get_by_uuid(self, uuid: UUID):
        if item := await self.repo.get_by_uuid(uuid):
            return item
        raise NotFoundException()
    
    async def delete_by_uuid(self, uuid: UUID):
        if item := await self.repo.delete_by_uuid(uuid):
            return item
        raise NotFoundException()
    
    async def get_all(self, limit: int, offset: int):
        if items := await self.repo.get_all(limit, offset):
            return items
        raise NotFoundException()