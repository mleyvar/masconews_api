# python
from email import message
import json
from turtle import title
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

from bussiness.pets import bussiness_access_pets, bussiness_add_new_user_pet, bussiness_add_pet, bussiness_show_all_pets
from bussiness.news import bussiness_access_news, bussiness_add_new, bussiness_add_new_user_news, bussiness_show_all_news
from model.AccessModel import AccessModel
from model.NewsModel import NewsModel
from model.PetModel import PetModel
from model.UserPetModel import UserPetModel

logger = logging.getLogger(__name__)
app = FastAPI(debug=True)

# path operations

# Root
@app.get("/")
def read_root():
    return {"message": "welcome to Service by Marco Polo Leyva!"}

### Show all pets
@app.get(
    path='/pets',
    status_code=status.HTTP_200_OK,
    summary="Show all Pets",
    tags=["Pets"]
    )
async def show_all_pets():
    return await bussiness_show_all_pets()

@app.post(
    path='/pet',
    status_code=status.HTTP_200_OK,
    summary="Add new Pet",
    tags=["Pets"]
    )
async def add_pet( new_pet: PetModel = Body(...)):
    return await bussiness_add_pet(logger, new_pet)


@app.post(
    path='/register_user_pet',
    status_code=status.HTTP_200_OK,
    summary="Add new User",
    tags=["Pets"]
    )
async def add_new_user_pet(new_user: UserPetModel = Body(...)):
    return await bussiness_add_new_user_pet(logger, new_user)

@app.post(
    path='/access_pet',
    status_code=status.HTTP_200_OK,
    summary="Access user pet",
    tags=["Pets"]
    )
async def access_pets(accessModel: AccessModel= Body(...)):
    return await bussiness_access_pets(accessModel)

### *********************************   NEWS


### Show all news
@app.get(
    path='/news',
    status_code=status.HTTP_200_OK,
    summary="Show all news",
    tags=["News"]
    )
async def show_all_news():
    return await bussiness_show_all_news()

@app.post(
    path='/news',
    status_code=status.HTTP_200_OK,
    summary="Add new News",
    tags=["News"]
    )
async def add_news( add_new: NewsModel = Body(...)):
    return await bussiness_add_new(add_new)


@app.post(
    path='/register_user_new',
    status_code=status.HTTP_200_OK,
    summary="Add new User",
    tags=["News"]
    )
async def add_new_user_news(new_user: UserPetModel = Body(...)):
    return await bussiness_add_new_user_news( new_user)


@app.post(
    path='/access_news',
    status_code=status.HTTP_200_OK,
    summary="Access user news",
    tags=["News"]
    )
async def access_news(accessModel: AccessModel= Body(...)):
    return await bussiness_access_news(accessModel)    