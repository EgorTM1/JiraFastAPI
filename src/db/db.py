from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from src.config import settings


engine = create_engine(
    url=settings.GET_URL
)

session_maker = sessionmaker(engine)

class Base(DeclarativeBase):
    pass
