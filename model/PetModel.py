#pydantic
from pydantic import BaseModel, EmailStr
from pydantic import Field
from pydantic import EmailStr


class PetModel(BaseModel):
    name: str = Field(
        ..., 
        max_length=50,
        min_length=1
        )
    type: str = Field(
        ..., 
        max_length=50,
        min_length=1
        )
    raza: str = Field(
        ..., 
        max_length=50,
        min_length=1
        )
    obs: str = Field(
        ..., 
        max_length=500,
        min_length=1
        )
