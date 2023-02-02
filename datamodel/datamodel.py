"""Datamodel Module."""


from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Users(Base):
    """Users Table."""

    __tablename__ = "users"

    userID = Column(Integer, primary_key=True)
    userName = Column(String)


class Times(Base):
    """Times Table."""

    __tablename__ = "times"

    timeID = Column(Integer, primary_key=True)
    timeValue = Column(DateTime)
    userID = Column(Integer, ForeignKey("users.userID"))
