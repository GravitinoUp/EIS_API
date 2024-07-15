"""
This class is used to interact with the database.
You can create your own or use it as a base class.
"""

from abc import ABC, abstractmethod
from uuid import UUID
from sqlalchemy import delete, insert, select, and_

from src.database import async_session_maker


class AbstractRepository(ABC):
    @abstractmethod
    async def add():
        raise NotImplementedError

    @abstractmethod
    async def get_all():
        raise NotImplementedError

    @abstractmethod
    async def get_by_id():
        raise NotImplementedError
    
    @abstractmethod
    async def get_by_uuid():
        raise NotImplementedError

    @abstractmethod
    async def get_by_data():
        raise NotImplementedError

    @abstractmethod
    async def delete_by_id():
        raise NotImplementedError
    
    @abstractmethod
    async def delete_by_uuid():
        raise NotImplementedError
    
    
class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add(self, data: dict):
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model)
            res = await session.execute(statement=stmt)
            await session.flush()
            await session.commit()
            return res.scalar_one()

    async def get_all(self):
        async with async_session_maker() as session:
            stmt = select(self.model)
            res = await session.execute(statement=stmt)
            return res.scalars().all()

    async def get_by_id(self, id: int):
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(id=id)
            res = await session.execute(statement=stmt)
            return res.scalar()
    
    async def get_by_uuid(self, uuid: UUID):
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(uuid=uuid)
            res = await session.execute(statement=stmt)
            return res.scalar()

    async def get_by_data(self, **filters):
        async with async_session_maker() as session:
            stmt = select(self.model).where(
                and_(
                    *[
                        getattr(self.model, key) == value for key, value in filters.items()
                    ]
                )
            )
            res = await session.execute(stmt)
            return res.scalar()

    async def delete_by_id(self, id: int):
        async with async_session_maker() as session:
            stmt = delete(self.model).filter_by(id=id).returning(self.model)
            res = await session.execute(statement=stmt)
            await session.commit()
            return res.scalar()
        
    async def delete_by_uuid(self, uuid: UUID):
        async with async_session_maker() as session:
            stmt = delete(self.model).filter_by(uuid=uuid).returning(self.model)
            res = await session.execute(statement=stmt)
            await session.commit()
            return res.scalar()