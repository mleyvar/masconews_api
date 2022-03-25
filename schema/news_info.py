from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from persistence.database import MyBase


class NewsInfo(MyBase):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    new = Column(String)
    url_image = Column(String)
