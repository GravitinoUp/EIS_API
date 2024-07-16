"""
purchase_events schemas
"""

from datetime import datetime
from uuid import UUID
from pydantic import BaseModel
from typing import Optional

# define your schemas here and rename< which already exists
class PurchaseEventCreateSchema(BaseModel):
    name: str
    created_at: Optional[datetime] = datetime.now()
    purchase_uuid: UUID
    user_uuid: UUID
    
    
class PurchaseEventGetSchema(PurchaseEventCreateSchema):
    uuid: UUID