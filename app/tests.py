#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------
# imports
# -------
from io import StringIO
from unittest import main, TestCase
from models import Restaurants, Locations, Food_types, Reviews
from insert_records import init_session, add_restaurant, add_location, add_food_type, add_review

session_token = init_session()

class test_db (TestCase):

    def test_1_restaurant_addition(self):
        global session_token

        add_restaurant(
                       session_token,
                       name = "Little Italy",
                       location = 78701,
                       price = "$$",
                       rating = "3",
                       hours = "9 to 5",
                       food_type = "Italian",
                       recent_review = "1"
                       )

        assert not (session_token.query(Restaurants), None)

    def test_2_Restaurants_manual_integrity(self):
        global session_token

        new_r = (
                name = "Little Italy 2",
                location = 78701,
                price = "$$",
                rating = "3",
                hours = "9 to 5",
                food_type = "Italian",
                recent_review = "1")
                )

       session_token.add(new_r)
       session_token.commit()
       assert not (session_token.query(Restaurants), None)

       restaurant_1 = session_token.query.filter
           (
           Restaurants.name == "Little Italy 2"
           )
       assert (restaurant_1.name == "Litte Italy 2")
       assert (restaurant_1.location == 78701)
       assert (restaurant_1.price == "$$")
       assert (restaurant_1.rating == 3)
       assert (restaurant_1.hours == "9 to 5")
       assert (restaurant_1.food_type == "Italian")
       assert (restaurant_1.recent_review == "1")

    def test_3_Restaurants_delete(self):
        global session_token
        new_r = (
                name = "Little Italy 2",
                location = 78701,
                price = "$$",
                rating = "3",
                hours = "9 to 5",
                food_type = "Italian",
                recent_review = "1")
                )

       session_token.add(new_r)
       session_token.commit()
       session_token.query.filter(Restaurants.name == "Little Italy 2").delete()
       assert (session_token.query.filter
               (
                Restaurants.name == "Little Italy 2"
               )               == None)

    def test_4_Locations_addition(self):
        global session_token

        add_restaurant(
                       session_token,
                       name = "Little Italy",
                       location = 78701,
                       price = "$$",
                       rating = "3",
                       hours = "9 to 5",
                       food_type = "Italian",
                       recent_review = "1"
                       )

        assert not (session_token.query(Restaurants), None)

    def test_5_Locations_manual_integrity(self):
        global session_token

        new_r = (
                name = "Little Italy 2",
                location = 78701,
                price = "$$",
                rating = "3",
                hours = "9 to 5",
                food_type = "Italian",
                recent_review = "1")
                )

       session_token.add(new_r)
       session_token.commit()
       assert not (session_token.query(Restaurants), None)

       restaurant_1 = session_token.query.filter
           (
           Restaurants.name == "Little Italy 2"
           )
       assert (restaurant_1.name == "Litte Italy 2")
       assert (restaurant_1.location == 78701)
       assert (restaurant_1.price == "$$")
       assert (restaurant_1.rating == 3)
       assert (restaurant_1.hours == "9 to 5")
       assert (restaurant_1.food_type == "Italian")
       assert (restaurant_1.recent_review == "1")

    def test_6_Locations_delete (self):
        global session_token
        new_r = (
                name = "Little Italy 2",
                location = 78701,
                price = "$$",
                rating = "3",
                hours = "9 to 5",
                food_type = "Italian",
                recent_review = "1")
                )

       session_token.add(new_r)
       session_token.commit()
       session_token.query.filter(Restaurants.name == "Little Italy 2").delete()
       assert (session_token.query.filter
               (
                Restaurants.name == "Little Italy 2"
               )               == None)

    def test_7_Reviews_addition(self):
        global session_token

        add_restaurant(
                       session_token,
                       name = "Little Italy",
                       location = 78701,
                       price = "$$",
                       rating = "3",
                       hours = "9 to 5",
                       food_type = "Italian",
                       recent_review = "1"
                       )

        assert not (session_token.query(Restaurants), None)

    def test_8_Reviews__manual_integrity(self):
        global session_token

        new_r = (
                name = "Little Italy 2",
                location = 78701,
                price = "$$",
                rating = "3",
                hours = "9 to 5",
                food_type = "Italian",
                recent_review = "1")
                )

       session_token.add(new_r)
       session_token.commit()
       assert not (session_token.query(Restaurants), None)

       restaurant_1 = session_token.query.filter
           (
           Restaurants.name == "Little Italy 2"
           )
       assert (restaurant_1.name == "Litte Italy 2")
       assert (restaurant_1.location == 78701)
       assert (restaurant_1.price == "$$")
       assert (restaurant_1.rating == 3)
       assert (restaurant_1.hours == "9 to 5")
       assert (restaurant_1.food_type == "Italian")
       assert (restaurant_1.recent_review == "1")

    def test_9_Reviews_delete (self):
        global session_token
        new_r = (
                name = "Little Italy 2",
                location = 78701,
                price = "$$",
                rating = "3",
                hours = "9 to 5",
                food_type = "Italian",
                recent_review = "1")
                )

       session_token.add(new_r)
       session_token.commit()
       session_token.query.filter(Restaurants.name == "Little Italy 2").delete()
       assert (session_token.query.filter
               (
                Restaurants.name == "Little Italy 2"
               )               == None)

    def test_10_Food_Type_addition(self):
        global session_token

        add_restaurant(
                       session_token,
                       name = "Little Italy",
                       location = 78701,
                       price = "$$",
                       rating = "3",
                       hours = "9 to 5",
                       food_type = "Italian",
                       recent_review = "1"
                       )

        assert not (session_token.query(Restaurants), None)

    def test_11_Food_Type_manual_Integrity (self):
        global session_token

        new_r = (
                name = "Little Italy 2",
                location = 78701,
                price = "$$",
                rating = "3",
                hours = "9 to 5",
                food_type = "Italian",
                recent_review = "1")
                )

       session_token.add(new_r)
       session_token.commit()
       assert not (session_token.query(Restaurants), None)

       restaurant_1 = session_token.query.filter
           (
           Restaurants.name == "Little Italy 2"
           )
       assert (restaurant_1.name == "Litte Italy 2")
       assert (restaurant_1.location == 78701)
       assert (restaurant_1.price == "$$")
       assert (restaurant_1.rating == 3)
       assert (restaurant_1.hours == "9 to 5")
       assert (restaurant_1.food_type == "Italian")
       assert (restaurant_1.recent_review == "1")

    def test_12_Food_Type_delete (self):
        global session_token
        new_r = (
                name = "Little Italy 2",
                location = 78701,
                price = "$$",
                rating = "3",
                hours = "9 to 5",
                food_type = "Italian",
                recent_review = "1")
                )

       session_token.add(new_r)
       session_token.commit()
       session_token.query.filter(Restaurants.name == "Little Italy 2").delete()
       assert (session_token.query.filter
               (
                Restaurants.name == "Little Italy 2"
               )               == None)
# ----
# main
# ----

if __name__ == "__main__":  # pragma: no cover
    main()
