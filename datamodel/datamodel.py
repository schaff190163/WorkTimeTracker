from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Users(Base):
    __tablename__ = "users"

    userID = Column(Integer, primary_key=True)
    userName = Column(String)


class Times(Base):
    __tablename__ = "times"

    timeID = Column(Integer, primary_key=True)
    timeValue = Column(DateTime)
    userID = Column(Integer, ForeignKey("users.userID"))
