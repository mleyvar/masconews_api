#pydantic
from pydantic import BaseModel, EmailStr
from pydantic import Field
from pydantic import EmailStr


class ResultModel(BaseModel):
    code: str = Field(
        ..., 
        max_length=5,
        min_length=1
        )
    message: str = Field(
        ..., 
        max_length=50,
        min_length=1
        )