from sqlalchemy import create_engine
from datamodel import Base

engine = create_engine('database.sql')
Base.metadata.create_all(engine)
