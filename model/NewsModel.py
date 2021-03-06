#pydantic
from typing import Optional
from fastapi import File
from pydantic import BaseModel, Field 

class NewsModel(BaseModel):
    title: str = Field(
        ..., 
        max_length=45,
        min_length=1
        )
    news: str = Field(
        ..., 
        max_length=2000,
        min_length=1
        )
    image: Optional[str] = Field(default=None)    
