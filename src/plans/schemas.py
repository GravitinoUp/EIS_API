"""
plans schemas
"""

from uuid import UUID
from pydantic import BaseModel


class PlanCreateSchema(BaseModel):
    year: int
    expense_type_code: int
    okpd2: str
    expense_total: float
    expense_fisrt_year: float
    expense_second_year: float
    expense_third_year: float
    expense_next_years: float


class PlanGetSchema(PlanCreateSchema):
    uuid: UUID



