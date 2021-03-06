
import base64
import email
import logging
from operator import contains
from unicodedata import name
import uuid
from bussiness.config.constants import BASE_PATH_IMAGE
from model.AccessModel import AccessModel
from model.PetModel import PetModel
from model.ResultAccessModel import ResultAccessModel
from model.ResultModel import ResultModel
from model.UserPetModel import UserPetModel
from schema.pets_info import PetsInfo
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from persistence.database import session
from schema.user_pets_info import  UserPetsInfo



async def bussiness_show_all_pets():
    #data = session.query(PetsInfo).all()
    data = []
    data.append(PetsInfo(id = 1, name= "Mascota 1", type="Perro", raza="Buldog", obs="detalle de la Mascota", url_image= BASE_PATH_IMAGE + "2a40c30a-fee8-4363-b1f5-394e5059a868.jpeg"))
    data.append(PetsInfo(id = 2, name= "Mascota 2", type="Perro", raza="Buldog", obs="detalle de la Mascota", url_image= BASE_PATH_IMAGE + "2a40c30a-fee8-4363-b1f5-394e5059a868.jpeg"))
    data.append(PetsInfo(id = 3, name= "Mascota 3", type="Perro", raza="Buldog", obs="detalle de la Mascota", url_image= BASE_PATH_IMAGE + "2a40c30a-fee8-4363-b1f5-394e5059a868.jpeg"))
    data.append(PetsInfo(id = 4, name= "Mascota 4", type="Perro", raza="Buldog", obs="detalle de la Mascota", url_image= BASE_PATH_IMAGE + "2a40c30a-fee8-4363-b1f5-394e5059a868.jpeg"))
    data.append(PetsInfo(id = 5, name= "Mascota 5", type="Perro", raza="Buldog", obs="detalle de la Mascota", url_image= BASE_PATH_IMAGE + "2a40c30a-fee8-4363-b1f5-394e5059a868.jpeg"))
    data.append(PetsInfo(id = 6, name= "Mascota 6", type="Perro", raza="Buldog", obs="detalle de la Mascota", url_image= BASE_PATH_IMAGE + "2a40c30a-fee8-4363-b1f5-394e5059a868.jpeg"))
    data.append(PetsInfo(id = 7, name= "Mascota 7", type="Perro", raza="Buldog", obs="detalle de la Mascota", url_image= BASE_PATH_IMAGE + "2a40c30a-fee8-4363-b1f5-394e5059a868.jpeg"))
    data.append(PetsInfo(id = 8, name= "Mascota 8", type="Perro", raza="Buldog", obs="detalle de la Mascota", url_image= BASE_PATH_IMAGE + "2a40c30a-fee8-4363-b1f5-394e5059a868.jpeg"))
    data.append(PetsInfo(id = 9, name= "Mascota 9", type="Perro", raza="Buldog", obs="detalle de la Mascota", url_image= BASE_PATH_IMAGE + "2a40c30a-fee8-4363-b1f5-394e5059a868.jpeg"))
    data.append(PetsInfo(id = 10, name= "Mascota 10", type="Perro", raza="Buldog", obs="detalle de la Mascota", url_image= BASE_PATH_IMAGE + "2a40c30a-fee8-4363-b1f5-394e5059a868.jpeg"))


    return data

async def bussiness_show_all_user_pets():
    #data = session.query(UserPetsInfo).all()
    data = []
    data.append(UserPetsInfo(email="sergio@admin.com", name="Sergio", last_name="El de Dulce", password="...."))

    return data


async def bussiness_access(accessModel: AccessModel):
    try:
        # print(accessModel)
        # data = session.query(UserPetsInfo).filter(UserPetsInfo.email == accessModel.email).one()
        data = UserPetsInfo(email="sergio@bancobase.com", name="Sergio", last_name="Martinez", password="Password123")
        # print(data)
        if data is None:
            return ResultAccessModel(code="-1", message="User or password invalid", user=getUserPetModalDefault())
        else:
            if data.password == accessModel.password:
                return ResultAccessModel(code="0", message="successfull", user=UserPetModel(email=data.email,
                                                                                            name=data.name,
                                                                                            last_name=data.last_name,
                                                                                            password="...."))
            else:
                return ResultAccessModel(code="-1", message="User or password invalid", user=getUserPetModalDefault())

    except Exception as e:
        # logger.info(e.detail)
        # print(e)
        session.rollback()
        if "No row was found" in str(e):
            return ResultModel(code="-1", message="Not exist the row")
        else:
            return ResultModel(code="-1", message="Error Server. Check Log")


async def bussiness_access_pets(accessModel: AccessModel):
    try:
        #print(accessModel)
        #data = session.query(UserPetsInfo).filter(UserPetsInfo.email == accessModel.email).one()
        data = UserPetsInfo(email= "sergio@admin.com", name="Sergio", last_name="El de Dulce", password ="Password123")
        #print(data)
        if data is  None:
            return ResultAccessModel(code="-1", message="User or password invalid", user= getUserPetModalDefault()) 
        else:
            if data.password == accessModel.password:
                return ResultAccessModel(code="0", message="successfull", user= UserPetModel(email = data.email,
                name= data.name, last_name=data.last_name, password="....")) 
            else:
                return ResultAccessModel(code="-1", message="User or password invalid", user= getUserPetModalDefault()) 
 
    except Exception as e:
                #logger.info(e.detail)
                #print(e)
                session.rollback()
                if "No row was found" in str(e):
                    return ResultModel(code="-1", message="Not exist the row") 
                else:    
                    return ResultModel(code="-1", message="Error Server. Check Log") 
    

async def bussiness_add_new_user_pet(user: UserPetModel):
    try:
        tempo_data = UserPetsInfo(
            email = user.email,
            name= user.name,
            last_name = user.last_name,
            password = user.password
        )
        
        #session.add(tempo_data)
        #session.flush()
        #session.commit()
        #session.close()

        return ResultModel(code="0", message="User inserted") 
    except Exception as e:
            #logger.info(e.detail)
            #print(e)
            session.rollback()

            return ResultModel(code="-1", message="Error Server. Check Log") 
    


async def bussiness_add_pet(new_pet: PetModel):
    try:

        decoded_image_data = base64.decodebytes(new_pet.image.encode('utf-8'))

        name = str(uuid.uuid4()) + ".jpeg" 
        open(f'images/{name}',"wb").write(decoded_image_data)
#        open(f'images/{name}',"wb").write(new_new.image.file.read())


        tempo_data = PetsInfo(
            name= new_pet.name,
            type = new_pet.type,
            raza = new_pet.raza,
            obs = new_pet.obs,
            url_image = BASE_PATH_IMAGE + name
        )
        
        #session.add(tempo_data)
        #session.flush()
        #session.commit()
        #session.close()

        return ResultModel(code="0", message="Pet inserted") 
    except Exception as e:
            print(e)
            session.rollback()

            return ResultModel(code="-1", message="Error Server. Check Log") 
    

def getUserPetModalDefault():
    return UserPetModel(email = ".",
    name= ".",
    last_name= ".",
    password=".")