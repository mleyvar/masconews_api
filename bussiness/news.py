
import base64
from typing import Optional
from fastapi import File, UploadFile
from bussiness.config.constants import BASE_PATH_IMAGE
from model.AccessModel import AccessModel
from model.NewsModel import NewsModel
from model.PetModel import PetModel
from model.ResultAccessModel import ResultAccessModel
from model.ResultModel import ResultModel
from model.UserNewModel import UserNewModel
from model.UserNewsModel import UserNewsModel
from schema.news_info import NewsInfo
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from persistence.database import session
from schema.user_news_info import UserNewsInfo

import uuid

async def bussiness_show_all_news():
    data = session.query(NewsInfo).all()

    return data



async def bussiness_add_new(new_new: NewsModel):
    try:
        print("image 1:")
        print(new_new.image)
        decoded_image_data = base64.decodebytes(new_new.image.encode('utf-8'))
        print("image 2:")

        name = str(uuid.uuid4()) + ".jpeg" 
        print("image 3:")
        open(f'images/{name}',"wb").write(decoded_image_data)
        print("image 4:")
#        open(f'images/{name}',"wb").write(new_new.image.file.read())

        tempo_data = NewsInfo(
            title= new_new.title,
            new = new_new.news,
            url_image = BASE_PATH_IMAGE + name
        )
        print("image 5:")
        
        session.add(tempo_data)
        print("image 6:")
        session.flush()
        print("image 7:")
        session.commit()
        print("image 8:")
        session.close()


        return ResultModel(code="0", message="New inserted") 
    except Exception as e:
            print(e)
            session.rollback()

            return ResultModel(code="-1", message="Error Server. Check Log") 
    




async def bussiness_add_new_user_news(user: UserNewsModel):
    try:
        tempo_data = UserNewsInfo(
            email = user.email,
            name= user.name,
            last_name = user.last_name,
            password = user.password
        )
        
        session.add(tempo_data)
        session.flush()
        session.commit()
        session.close()

        return ResultModel(code="0", message="User inserted") 
    except Exception as e:
            #logger.info(e.detail)
            #print(e)
            session.rollback()

            return ResultModel(code="-1", message="Error Server. Check Log") 
    




async def bussiness_access_news(accessModel: AccessModel):
    try:
        #print(accessModel)
        data = session.query(UserNewsInfo).filter(UserNewsInfo.email == accessModel.email).one()
        #print(data)
        if data is  None:
            return ResultAccessModel(code="-1", message="User or password invalid", user= getUserNewModalDefault()) 
        else:
            if data.password == accessModel.password:
                return ResultAccessModel(code="0", message="successfull", user= UserNewModel(email = data.email,
                name= data.name, last_name=data.last_name, password="....")) 
            else:
                return ResultAccessModel(code="-1", message="User or password invalid", user= getUserNewModalDefault()) 
 
    except Exception as e:
                #logger.info(e.detail)
                #print(e)
                session.rollback()
                if "No row was found" in str(e):
                    return ResultModel(code="-1", message="Not exist the row") 
                else:    
                    return ResultModel(code="-1", message="Error Server. Check Log") 
    


def getUserNewModalDefault():
    return UserNewModel(email = ".",
    name= ".",
    last_name= ".",
    password=".")