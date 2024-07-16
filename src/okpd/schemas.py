"""
okpd schemas
"""

from uuid import UUID
from pydantic import BaseModel


# define your schemas here and rename< which already exists
class OKPDCreateShcema(BaseModel):
    name: str
    code: str
    data: str
    

class OKPDGetSchema(OKPDCreateShcema):
    uuid: UUID