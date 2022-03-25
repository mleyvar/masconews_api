#pydantic
from pydantic import BaseModel, EmailStr
from pydantic import Field
from pydantic import EmailStr

class AccessModel(BaseModel):
    email: str = Field(
        ..., 
        min_length=1,
        max_length=50,
         example ="xxxx@yyy.com"
        )
    password: str = Field(
        ..., 
        min_length=1,
        max_length=50,
        example ="Passw0rd1!"
        )
