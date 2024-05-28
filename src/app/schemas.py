# File for the schemas and validation

from typing import Optional
from pydantic import BaseModel, Field

class Acquisition(BaseModel):
    id: Optional[int] = None
    budget: float
    unit: str
    acq_type: str
    quantity: int
    cost_per_unit: float
    total_value: float
    adquisition_date: str
    supplier: str
    documentation: Optional[str]
    
class UpdateAcquisition(BaseModel):
    budget: Optional[float]
    unit: Optional[str]
    ac_type: Optional[str]
    quantity: Optional[int]
    cost_per_unit: Optional[float]
    total_value: Optional[float]
    adquisition_date: Optional[str]
    supplier: Optional[str]
    documentation: Optional[str]


class SearchAcquisition(BaseModel):
    budget: Optional[float] = None
    unit: Optional[str] = None
    ac_type: Optional[str] = None
    quantity: Optional[int] = None
    cost_per_unit: Optional[float] = None
    total_value: Optional[float] = None
    adquisition_date: Optional[str] = None
    supplier: Optional[str] = None


class Record(BaseModel):
    update_details: str
    record_date: str

#  @field_validator('id', 'name')
#     @classmethod
#     def check_alphanumeric(cls, v: str, info: ValidationInfo) -> str:
#         if isinstance(v, str):
#             # info.field_name is the name of the field being validated
#             is_alphanumeric = v.replace(' ', '').isalnum()
#             assert is_alphanumeric, f'{info.field_name} must be alphanumeric'
#         return v