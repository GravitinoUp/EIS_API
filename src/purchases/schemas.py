"""
purchase schemas
"""

from typing import Optional
from uuid import UUID
from pydantic import BaseModel

from src.purchases.models import Purchase


class OrgnizationSchema(BaseModel):
    name: str
    inn: str
    kpp: str
    okpo: str


class PurchaseCreateSchema(BaseModel):
    year: int
    expense_type_code: int
    okpd2: int

    expense_total: float
    expense_first_year: float
    expense_second_year: float
    expense_third_year: float
    expense_next_years: float
    
    organization: Optional[OrgnizationSchema]
    
    def custom_dict(self):
        return {
            "year": self.year,
            "expense_type_code": self.expense_type_code,
            "okpd2": self.okpd2,
            "expense_total": self.expense_total,
            "expense_first_year": self.expense_first_year,
            "expense_second_year": self.expense_second_year,
            "expense_third_year": self.expense_third_year,
            "expense_next_years": self.expense_next_years,
            "organization_name": self.organization.name,
            "organization_inn": self.organization.inn,
            "organization_kpp": self.organization.kpp,
            "organization_okpo": self.organization.okpo
        }
        
    @classmethod
    def from_model(cls, purchase: Purchase):
        purchase_dict = purchase.__dict__
        org_name = purchase_dict.pop('organization_name')
        org_inn = purchase_dict.pop('organization_inn')
        org_kpp = purchase_dict.pop('organization_kpp')
        org_okpo = purchase_dict.pop('organization_okpo')
        return cls(
            **purchase_dict, 
            organization=OrgnizationSchema(
                name=org_name,
                inn=org_inn,
                kpp=org_kpp,
                okpo=org_okpo   
            )
        )
    
    
class PurchaseGetSchema(PurchaseCreateSchema):
    uuid: UUID
    status: str

