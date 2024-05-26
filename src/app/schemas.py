# File for the schemas and validation

from typing import Optional
from pydantic import BaseModel, Field

class Acquisition(BaseModel):
    budget: float
    unit: str
    ac_type: str
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
    budget: Optional[float]
    unit: Optional[str]
    ac_type: Optional[str]
    quantity: Optional[int]
    cost_per_unit: Optional[float]
    total_value: Optional[float]
    adquisition_date: Optional[str]
    supplier: Optional[str]


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