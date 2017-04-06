from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
def init_session(engine):
    Base.metadata.bind = engine
    return sessionmaker(bind=engine)

def setupdb(engine):
    Base.metadata.create_all(engine)
