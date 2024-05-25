# File for the schemas and validation

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
    documentation: str


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