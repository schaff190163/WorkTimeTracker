"""Create Database File."""


from sqlalchemy import create_engine

from datamodel import Base

engine = create_engine('sqlite:///C:\\Users\\Simon\\OneDrive\\Dokumente\\4AHIT\\SEW INSY\\WorkTimeTracker\\datamodel\\app_db.sql')
Base.metadata.create_all(engine)
