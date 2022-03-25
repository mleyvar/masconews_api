# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://newappsc_masconews:BD_vZ8tWzL3d@setcoding.com/newappsc_masconews"

db_engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

session = SessionLocal()
MyBase = declarative_base(db_engine)



