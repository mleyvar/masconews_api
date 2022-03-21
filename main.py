# python
from email import message
import json
from uuid import UUID
from datetime import date
from datetime import datetime
from typing import Optional, List


import logging
import logging.config

# pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

# FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import Body

logger = logging.getLogger(__name__)
app = FastAPI(debug=True)

# Models
class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field (..., min_length=8)

class User(UserBase):
    password: str = Field (..., min_length=8)
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    birth_date: Optional[date] = Field(default=None)    

class UserRegisterRecipe(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    email: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    password: str = Field (..., min_length=8)
    birth_date: Optional[date] = Field(default=None)    


class UserRegister(User):
       password: str = Field (..., min_length=8)

class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ..., 
        max_length=253,
        min_length=1
        )
    created_at: datetime = Field(default=datetime.now())    
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)    
    

class Recipe(BaseModel):
    recipe_id: UUID = Field(...)
    title: str = Field(
        ..., 
        max_length=500,
        min_length=1
        )
    detail: str = Field(
        ..., 
        max_length=1250,
        min_length=1
        )
    image_url: str = Field(
        ..., 
        min_length=1
        )
    author: str = Field(
        ..., 
        min_length=1
        )
        
    created_at: datetime = Field(default=datetime.now())    
    
class UserRecipe(BaseModel):
    user_id: UUID = Field(...)
    user: str = Field(
        ..., 
        max_length=25,
        min_length=1
        )
    password: str = Field(
        ..., 
        max_length=25,
        min_length=1
        )
    created_at: datetime = Field(default=datetime.now())    


    
class Result(BaseModel):
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
    
class AccessResponse(BaseModel):
    result: Result = Field(...)


# path operations


### Show all users
@app.get(
    path='/pets',
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all Pets",
    tags=["Pets"]
    )
def show_all_pets():
    return {"Hello": "World"}

