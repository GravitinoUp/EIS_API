"""
okpd app service and repository
"""

from src.abstract_repository import SQLAlchemyRepository, AbstractRepository


# define your service here and rename if it's necessary
# WARNING: if this sevice doesn't work with DB,
# you may implement only your own service

class ItemRepository(SQLAlchemyRepository):
    # model = YourModel (import from models)
    ...


class ItemService:
    def __init__(self, repository: AbstractRepository):
        self.repository: AbstractRepository = repository()
