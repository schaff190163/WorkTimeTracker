from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Users(Base):
    tablename = "users"

    userID = Column(Integer, primary_key=True)
    userName = Column(String)


class Times(Base):
    tablename = "uimes"

    timeID = Column(Integer, primary_key=True)
    timeValue = Column(int)
    userID = Column(DateTime, ForeignKey("users.userID"))
