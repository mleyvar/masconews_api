#pydantic
from pydantic import BaseModel, EmailStr
from pydantic import Field
from pydantic import EmailStr

class UserNewModel(BaseModel):
    email: str = Field(
        ..., 
        min_length=1,
        max_length=50,
         example ="xxxx@yyy.com"
        )
    name: str = Field(
        ..., 
        min_length=1,
        max_length=50,
        example ="FAcundo"
        )
    last_name: str = Field(
        ..., 
        min_length=1,
        max_length=50,
        example ="Perez"
        )
    password: str = Field(
        ..., 
        min_length=1,
        max_length=50,
        example ="Passw0rd1!"
        )
