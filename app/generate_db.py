from db_manager import init_session, setupdb
from sqlalchemy import create_engine
from insert_records import add_restaurant

db_name = 'sqlite:///food_close_to.db'
db_engine = create_engine(db_name)
setupdb(db_engine)
session_token = init_session(db_engine)

# TODO populate all restaurants
with open("one2oneMega.json", "r") as m:
    for key in m:
        add_restaurant (session_token,
                        name=m[key]["name"],
                        location=m[key]["location"]["zip_code"],
                        price=m[key]["price"],
                        rating= float(m[key]["rating"]),
                        food_type= m[key][]
                        )



# TODO populate all reviews

# TODO populate all Locations (tedious)

# TODO populate all food types
