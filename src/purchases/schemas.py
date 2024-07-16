"""
purchases schemas
"""

from datetime import datetime
from uuid import UUID
from pydantic import BaseModel
from typing import Optional


# define your schemas here and rename< which already exists
class PurchaseCreateSchema(BaseModel):
    plan_uuid: UUID
    name: str
    kosgu_uuid: UUID
    purchase_offer_number: Optional[int]
    okpd_uuid: UUID
    object_name: str
    okei_id: int
    result_name: Optional[str]
    npa_date: datetime
    npa_number: str
    start_max_price: float
    limit_uuid: UUID
    purchase_public_discussion: Optional[str]
    authorized_instution: Optional[str]
    organizer_name: Optional[str]
    placement_month: Optional[int] 
    way_id: int
    small_buisness: Optional[str]
    price_value: float
    savings: Optional[float]
    contract_number: str
    contract_date: datetime
    contragent: Optional[str]
    approval_letter: Optional[str]
    purchase_type_uuid: UUID
    initiator_uuid: UUID    
    executor_uuid: UUID
    purchase_id: int
    contract_id: int
    start_date: datetime
    end_application_date: Optional[datetime]
    executor_date: Optional[datetime]
    end_date: datetime
    end_price: float
    currency_code: str
    purchase_step_uuid: UUID
    delivery_address: Optional[str]
    is_organization_fund: Optional[bool]
    application_enforcement: Optional[str]
    is_unilateral_refusion: Optional[bool]
    contract_enforcement: Optional[str]
    quality_gurantee_period: Optional[int]
    manufacturer_guarantee: Optional[int]
    warranty_obligations_enforcement: Optional[str]
    additionl_info: Optional[str] 
    

class PurchaseGetShcema(PurchaseCreateSchema):
    uuid: UUID
    