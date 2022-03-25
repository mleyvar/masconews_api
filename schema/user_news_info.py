from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from persistence.database import MyBase


class UserNewsInfo(MyBase):
    __tablename__ = "user_news"

    email = Column(String, primary_key=True, index=True)
    name = Column(String)
    last_name = Column(String)
    password = Column(String)
