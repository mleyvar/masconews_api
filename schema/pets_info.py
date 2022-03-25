from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from persistence.database import MyBase


class PetsInfo(MyBase):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    raza = Column(String)
    obs = Column(String)
    url_image = Column(String)
