from db_manager import init_session, setupdb
from sqlalchemy import create_engine

db_name = 'sqlite:///food_close_to.db'
db_engine = create_engine(db_name)
setupdb(db_engine)
session_token = init_session(db_engine)

# TODO populate all restaurants

# TODO populate all reviews

# TODO populate all Locations (tedious)

# TODO populate all food types
