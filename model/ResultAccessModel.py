#pydantic
from pydantic import BaseModel, EmailStr
from pydantic import Field
from pydantic import EmailStr

from model.ResultModel import ResultModel
from model.UserPetModel import UserPetModel


class ResultAccessModel(ResultModel):
    user: UserPetModel = Field(...)
   