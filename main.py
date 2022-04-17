# python


import logging
import logging.config
from typing import Optional
import uuid
from fastapi.middleware.cors import CORSMiddleware

# FastAPI
from fastapi import FastAPI, File, UploadFile
from fastapi import status
from fastapi import Body

from bussiness.pets import bussiness_access_pets, bussiness_add_new_user_pet, bussiness_add_pet, \
    bussiness_show_all_pets, bussiness_show_all_user_pets, bussiness_access
from bussiness.news import bussiness_access_news, bussiness_add_new, bussiness_add_new_user_news, bussiness_show_all_news, bussiness_show_all_users_news
from model.AccessModel import AccessModel
from model.NewsModel import NewsModel
from model.PetModel import PetModel
from model.UserPetModel import UserPetModel
from fastapi.staticfiles import StaticFiles


logger = logging.getLogger(__name__)
app = FastAPI(debug=True)
app.mount("/images", StaticFiles(directory="images"), name="images")


origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# path operations

# Root
@app.get("/")
def read_root():
    return {"message": "welcome to Service by Marco Polo Leyva!"}

@app.post(
    path='/auth/access',
    status_code=status.HTTP_200_OK,
    summary="Access "
    )
async def access(accessModel: AccessModel= Body(...)):
    return await bussiness_access(accessModel)

### Show all pets
@app.get(
    path='/pets',
    status_code=status.HTTP_200_OK,
    summary="Show all Pets",
    tags=["Pets"]
    )
async def show_all_pets():
    return await bussiness_show_all_pets()

@app.get(
    path='/users_pet',
    status_code=status.HTTP_200_OK,
    summary="Show all Users from Pets",
    tags=["Pets"]
    )
async def show_all_user_pets():
    return await bussiness_show_all_user_pets()

@app.post(
    path='/pet',
    status_code=status.HTTP_200_OK,
    summary="Add new Pet",
    tags=["Pets"]
    )
async def add_pet( new_pet: PetModel = Body(...)):
    return await bussiness_add_pet(new_pet)


@app.post(
    path='/register_user_pet',
    status_code=status.HTTP_200_OK,
    summary="Add new User",
    tags=["Pets"]
    )
async def add_new_user_pet(new_user: UserPetModel = Body(...)):
    return await bussiness_add_new_user_pet(new_user)

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

@app.get(
    path='/users_news',
    status_code=status.HTTP_200_OK,
    summary="Show all users from news",
    tags=["News"]
    )
async def show_all_users_news():
    return await bussiness_show_all_users_news()

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




@app.post(
    path="/post-image",
    status_code=status.HTTP_200_OK,
    tags=["Instagram"]
)
def post_image(
    image: UploadFile = File(...)
):

   if (image == None):
        return {"result":"no file exist"}
   else: 
        name = str(uuid.uuid4()) + ".jpeg" 
        print(image.file)
        print(image.filename)

        print(name)
        open(f'images/{name}',"wb").write(image.file.read())
    # with open(f'images/{image.filename}', "wb") as buffer:


        return {
            "result": "Success",
            "filename": name,
            "format": image.content_type,
            "size(kb)": round(len(image.file.read())/1024, ndigits=2)
        }

