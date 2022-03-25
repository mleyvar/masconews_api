
import email
import logging
from operator import contains
from unicodedata import name
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
    data = session.query(PetsInfo).all()

    return data


async def bussiness_access_pets(accessModel: AccessModel):
    try:
        #print(accessModel)
        data = session.query(UserPetsInfo).filter(UserPetsInfo.email == accessModel.email).one()
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
    


async def bussiness_add_pet(new_pet: PetModel):
    try:
        tempo_data = PetsInfo(
            name= new_pet.name,
            type = new_pet.type,
            raza = new_pet.raza,
            obs = new_pet.obs,
        )
        
        session.add(tempo_data)
        session.flush()
        session.commit()
        session.close()

        return ResultModel(code="0", message="Pet inserted") 
    except Exception as e:
            #print(e)
            session.rollback()

            return ResultModel(code="-1", message="Error Server. Check Log") 
    

def getUserPetModalDefault():
    return UserPetModel(email = ".",
    name= ".",
    last_name= ".",
    password=".")