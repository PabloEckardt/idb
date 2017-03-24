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
        '''
        Testing our Wrapper to add records on Restaurants

        '''
        add_restaurant(
                       session_token,
                       name="Little Italy",
                       location=78701,
                       price="$$",
                       rating="3",
                       hours="9 to 5",
                       food_type="Italian",
                       recent_review="1"
                       )

        assert not (session_token.query(Restaurants) is None)

    def test_2_Restaurants_manual_integrity(self):
        '''
        Testing query data on Restaurants

        '''
        global session_token

        new_r = Restaurants(
                name="Little Italy 2",
                location=78701,
                price=2,
                rating=3,
                hours="9 to 5",
                food_type="Italian",
                recent_review="1")
                )

       session_token.add(new_r)
       session_token.commit()

       restaurant_1=session_token.query(Restaurants).filter_by(name == "Little Italy\
                                                                  2").first()

       assert not (session_token.query(Restaurants) is None)

       assert (restaurant_1.name == "Litte Italy 2")
       assert (restaurant_1.location == 78701)
       assert (restaurant_1.price == 2)
       assert (restaurant_1.rating == 3)
       assert (restaurant_1.hours == "9 to 5")
       assert (restaurant_1.food_type == "Italian")
       assert (restaurant_1.recent_review == "1")

    def test_3_Restaurants_delete(self):
        '''
        Testing Deletion of Records on Restaurants

        '''
        global session_token
        new_r=Restaurants(
                name = "Little Italy 3",
                location = 78701,
                price = "$$",
                rating = "3",
                hours = "9 to 5",
                food_type = "Italian",
                recent_review = "1")
                )

        session_token.add(new_r)
        session_token.commit()

        rst=session_token.query(Restaurants).filter_by(
            name="Little Italy 3").first()

        session_token.delete(rst)
        session_token.commit()

        rst=session_token.query(Restaurants).filter_by(
            name="Little Italy 3").first()

        assert (rst is None)

    def test_4_Locations_addition(self):
        global session_token
        '''
        Testing our Wrapper to add records on Locations

        '''
        add_Location(
                        session_token,
                        zipcode=77777,
                        average_rating=3,
                        average_price=2,
                        adjacent_location=77778,
                        average_health_rating=88,
                        highest_price="$$",
                        popular_food_type="Italian",
                        highest_rated_restaurant="Little Italy"
                     )

        assert not (session_token.query(Locations) is None)

    def test_5_Locations_manual_integrity(self):
        global session_token
        '''
        Testing query data on Locations

        '''
        global session_token

        new_l=Locations(
                session_token,
                zipcode=77777,
                average_rating=3,
                average_price=2,
                adjacent_location=77778,
                average_health_rating=88,
                highest_price="$$",
                popular_food_type="Italian",
                highest_rated_restaurant="Little Italy"
                )

       session_token.add(new_l)
       session_token.commit()

       loc=session_token.query(Locations).filter_by(zipcode == 77777).first()

       assert not (session_token.query(Locations) is None)

       assert (loc.zipcode == 77777)
       assert (loc.average_rating == 3)
       assert (loc.average_price == 2)
       assert (loc.adjacent_location == 77778)
       assert (loc.highest_price == "$$")
       assert (loc.popular_food_type == "Italian")
       assert (loc.highest_rated_restaurant == "Little Italy")


    def test_6_Locations_delete(self):
        global session_token
        '''
        Testing Deletion of Records on Locations

        '''
        global session_token

        new_l=Locations(
                session_token,
                zipcode=77776,
                average_rating=3,
                average_price=2,
                adjacent_location=77778,
                average_health_rating=88,
                highest_price="$$",
                popular_food_type="Italian",
                highest_rated_restaurant="Little Italy"
                )

        session_token.add(new_l)
        session_token.commit()

        l=session_token.query(Locations).filter_by(zipcode=77776).first()

        session_token.delete(l)
        session_token.commit()

        l=session_token.query(Locations).filter_by(zipcode=77776).first()

        assert (l is None)

    def test_7_Reviews_addition(self):
        global session_token
        '''
        Testing our Wrapper to add records on Reviews

        '''
        add_review(
                    session_token,
                    date="12/1/2014",
                    rating=4,
                    username="pebs",
                    profile_picture_url="/review_profiles/pebs",
                    restaurant_pictures_url="/reviews_images/pebs/1",
                    restaurant_id=1,
                    zipcode=77777
                    )

        assert not (session_token.query(Reviews) is None)

    def test_8_Reviews__manual_integrity(self):
        global session_token
        '''
        Testing query data on Reviews

        '''
        global session_token

        new_r=Reviews(
                    session_token,
                    date="12/1/2014",
                    rating=4,
                    username="pebs",
                    profile_picture_url="/review_profiles/pebs",
                    restaurant_pictures_url="/reviews_images/pebs/1",
                    restaurant_id=1,
                    zipcode=67777
                )

       session_token.add(new_r)
       session_token.commit()

       rev=session_token.query(Reviews).filter_by(review_id=1).first()

       assert not (session_token.query(Reviews) is None)

       assert (rev.zipcode == 67777)
       assert (rev.date == "12/1/2014")
       assert (rev.rating == 4)
       assert (rev.username == "pebs")
       assert (rev.profile_picture_url == "/review_profiles/pebs")
       assert (rev.restaurant_pictures_url == "/reviews_images/pebs/1")
       assert (rev.restaurant_id == 1)

    def test_9_Reviews_delete(self):
        global session_token
        '''
        Testing Deletion of Records on Reviews

        '''
        global session_token

        new_r=Reviews(
                    session_token,
                    date="12/1/2014",
                    rating=4,
                    username="pebs",
                    profile_picture_url="/review_profiles/pebs",
                    restaurant_pictures_url="/reviews_images/pebs/1",
                    restaurant_id=1,
                    zipcode=67777
                )

        session_token.add(new_r)
        session_token.commit()

        r=session_token.query(Reviews).filter_by(review_id=1).first()

        session_token.delete(r)
        session_token.commit()

        r=session_token.query(Locations).filter_by(review_id=1).first()

        assert (r is None)

    def test_10_Food_Type_addition(self):
        global session_token
        '''
        Testing our Wrapper to add records on Food Types

        '''
        add_food_type(
                        session_token,
                        food_type="Italian",
                        average_price=3,
                        average_rating=3,
                        country_of_origin="Italy",
                        image_url="/food_types/italian/",
                        open_restaurants=1,
                        highest_rated_restaurant="Little Italy",
                        best_location=78787
                      )

        assert not (session_token.query(Food_Types) is None)

    def test_11_Food_Type_manual_Integrity(self):
        global session_token
        '''
        Testing query data on Food Types

        '''
        global session_token

        new_f=Food_Types(
                        session_token,
                        food_type="Italian",
                        average_price=3,
                        average_rating=3,
                        country_of_origin="Italy",
                        image_url="/food_types/italian/",
                        open_restaurants=1,
                        highest_rated_restaurant="Little Italy",
                        best_location=78787
                           )

       session_token.add(new_f)
       session_token.commit()

       food=session_token.query(Food_Types).filter_by(
           food_type="Italian").first()

       assert not (session_token.query(Food_Types) is None)

       assert (food.food_type == "Italian")
       assert (food.average_price == 3)
       assert (food.rating == 3)
       assert (food.country_of_origin == "Italy")
       assert (food.image_url == "/food_types/italian/")
       assert (food.open_restaurants == 1)
       assert (food.highest_rated_restaurant == "Little Italy")
       assert (food.best_location == 78787)

    def test_12_Food_Type_delete(self):
        global session_token
        '''
        Testing Deletion of Records on Food Types

        '''
        global session_token

        new_f=Food_Types(
                        session_token,
                        food_type="Italian",
                        average_price=3,
                        average_rating=3,
                        country_of_origin="Italy",
                        image_url="/food_types/italian/",
                        open_restaurants=1,
                        highest_rated_restaurant="Little Italy",
                        best_location=78787
                        )

        session_token.add(new_f)
        session_token.commit()

        f=session_token.query(Food_Types).filter_by(
            food_type="Italian").first()

        session_token.delete(f)
        session_token.commit()

        f=session_token.query(Food_Types).filter_by(
            food_type="Italian").first()

        assert (f is None)
# ----
# main
# ----

if __name__ == "__main__":  # pragma: no cover
    main()