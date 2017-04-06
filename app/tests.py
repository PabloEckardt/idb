#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------
# imports
# -------
import json
from flask import current_app as app
from io import StringIO
from unittest import main, TestCase
from models import Restaurants, Locations, Food_Types, Reviews
from insert_records import add_restaurant, add_location, add_food_type, add_review
from sqlalchemy import create_engine
from db_manager import *



class test_db (TestCase):

    db_name = 'sqlite:///testdb.db'
    testEngine = create_engine(db_name)
    setupdb(testEngine)
    session_token = init_session(testEngine)

    def test_1_restaurant_addition(self):
        '''
        Testing our Wrapper to add records on Restaurants

        '''
        add_restaurant(
                        self.session_token,
                        id=u"0001",
                        name=u"Little Italy",
                        yelp_id=u"little_italy",
                        location=78701,
                        lat=1.0000,
                        long=1.0000,
                        city=u"Austin",
                        address=u"123 f",
                        phone=u"(512)123123",
                        price=u"$",
                        rating=3.0,
                        review=u"test_review",
                        review_date=u"Today",
                        review_count=123,
                        url=u"www.web.com",
                        img_url=u"www.web.com/img.jpg",
                        food_types=[u"Italian"]
                      )

        assert not (self.session_token.query(Restaurants) is None)

    def test_2_Restaurants_manual_integrity(self):
        '''
        Testing query data on Restaurants

        '''
        
        new_r = Restaurants(
                id="0002",
                name="Little Italy2",
                yelp_id="little_italy",
                location=78701,
                lat=1.0000,
                long=1.0000,
                city="Austin",
                address="123 f",
                phone="(512)123123",
                price="$",
                rating=3.0,
                review="test_review",
                review_date="Today",
                review_count=123,
                url="www.web.com",
                img_url="www.web.com/img.jpg",
                food_type="Italian"
                )

        self.session_token.add(new_r)
        self.session_token.commit()

        restaurant_1=self.session_token.query(Restaurants).filter_by(
            name = "Little Italy2").first()

        assert not (self.session_token.query(Restaurants) is None)
        assert restaurant_1.id == "0002"
        assert restaurant_1.name == "Little Italy2"
        assert restaurant_1.location == 78701
        assert restaurant_1.lat==1.0000
        assert restaurant_1.long==1.0000
        assert restaurant_1.city=="Austin"
        assert restaurant_1.price == "$"
        assert restaurant_1.rating == 3.0
        assert restaurant_1.food_type == "Italian"
        assert restaurant_1.Review == "test_review"
        assert restaurant_1.Review_Date == "Today"

    def test_3_Restaurants_delete(self):
        global session_token
        '''
        Testing Deletion of Records on Restaurants

        '''

        new_r = Restaurants(
                id="0003",
                name="Little Italy3",
                yelp_id="little_italy",
                location=78701,
                lat=1.0000,
                long=1.0000,
                city="Austin",
                address="123 f",
                phone="(512)123123",
                price="$",
                rating=3.0,
                review="test_review",
                review_date="Today",
                review_count=123,
                url="www.web.com",
                img_url="www.web.com/img.jpg",
                food_type="Italian"
        )

    """
        self.session_token.add(new_r)
        self.session_token.commit()

        rst=self.session_token.query(Restaurants).filter_by(
            name="Little Italy 3").first()

        self.session_token.delete(rst)
        self.session_token.commit()

        rst=self.session_token.query(Restaurants).filter_by(
            name="Little Italy 3").first()

        assert (rst is None)

    def test_4_Locations_addition(self):
        
        '''
        Testing our Wrapper to add records on Locations

        '''
        global session_token
        add_location(
                        self.session_token,
                        average_rating=3,
                        average_price=2,
                        zipcode=77777,
                        highest_price=2,
                        popular_food_type="Italian",
                        highest_rated_restaurant="Little Italy"
                     )

        assert not (self.session_token.query(Locations) is None)

    def test_5_Locations_manual_integrity(self):
        
        '''
        Testing query data on Locations

        '''
        

        new_l=Locations(
                zipcode=77776,
                average_rating=3,
                average_price=2,
                highest_price=2,
                popular_food_type="Italian",
                highest_rated_restaurant="Little Italy"
                )

        self.session_token.add(new_l)
        self.session_token.commit()

        loc=self.session_token.query(Locations).filter_by(zipcode = 77777).first()

        assert not (self.session_token.query(Locations) is None)

        assert (loc.zipcode == 77777)
        assert (loc.average_rating == 3)
        assert (loc.average_price == 2)
        assert (loc.highest_price == 2)
        assert (loc.popular_food_type == "Italian")
        assert (loc.highest_rated_restaurant == "Little Italy")


    def test_6_Locations_delete(self):
        
        '''
        Testing Deletion of Records on Locations

        '''
        

        new_l=Locations(
                zipcode=11111,
                average_rating=3,
                average_price=2,
                highest_price= 2,
                popular_food_type="Italian",
                highest_rated_restaurant="Little Italy"
                )

        self.session_token.add(new_l)
        self.session_token.commit()

        l=self.session_token.query(Locations).filter_by(zipcode=11111).first()

        self.session_token.delete(l)
        self.session_token.commit()

        l=self.session_token.query(Locations).filter_by(zipcode=11111).first()

        assert (l is None)

    def test_7_Reviews_addition(self):
        
        '''
        Testing our Wrapper to add records on Reviews

        '''
        add_review(
                    self.session_token,
                    date="12/1/2014",
                    rating=4,
                    username="pebs",
                    profile_picture_url="/review_profiles/pebs",
                    review_url="/review/1",
                    restaurant_id=1,
                    zipcode=77777
                    )

        assert not (self.session_token.query(Reviews) is None)

    def test_8_Reviews__manual_integrity(self):
        
        '''
        Testing query data on Reviews

        '''
        

        new_r=Reviews(
                    date="12/1/2014",
                    rating=4,
                    username="pebs",
                    profile_picture_url="/review_profiles/pebs",
                    review_url="/review/1",
                    restaurant_id=1,
                    zipcode=67778
                )

        self.session_token.add(new_r)
        self.session_token.commit()

        rev=self.session_token.query(Reviews).filter_by(review_id=2).first()

        assert not (self.session_token.query(Reviews) is None)

        assert (rev.zipcode == 67778)
        assert (rev.date == "12/1/2014")
        assert (rev.rating == 4)
        assert (rev.username == "pebs")
        assert (rev.profile_picture_url == "/review_profiles/pebs")
        assert (rev.review_url == "/review/1")
        assert (rev.restaurant_id == 1)

    def test_9_Reviews_delete(self):
        
        '''
        Testing Deletion of Records on Reviews

        '''
        

        new_r=Reviews(
                    date="12/1/2014",
                    rating=4,
                    username="pebs",
                    profile_picture_url="/review_profiles/pebs",
                    review_url="/reviews_images/pebs/1",
                    restaurant_id=1,
                    zipcode=67777
                )

        self.session_token.add(new_r)
        self.session_token.commit()

        r=self.session_token.query(Reviews).filter_by(review_id=3).first()

        self.session_token.delete(r)
        self.session_token.commit()

        r=self.session_token.query(Reviews).filter_by(review_id=3).first()

        assert (r is None)

    def test_10_Food_Type_addition(self):
        
        '''
        Testing our Wrapper to add records on Food Types

        '''
        global session_token
        add_food_type(
                        self.session_token,
                        food_type="Italian",
                        average_price=3,
                        average_rating=3,
                        image_url="/food_types/italian/",
                        highest_rated_restaurant=92834,
                        best_location=78787
                      )

        assert not (self.session_token.query(Food_Types) is None)

    def test_11_Food_Type_manual_Integrity(self):
        
        '''
        Testing query data on Food Types

        '''
        

        new_f=Food_Types(
                        food_type="Italian2",
                        average_price=3,
                        average_rating=3,
                        image_url="/food_types/italian/",
                        highest_rated_restaurant= 123,
                        best_location=78787
                           )

        self.session_token.add(new_f)
        self.session_token.commit()

        food=self.session_token.query(Food_Types).filter_by(
           food_type="Italian2").first()

        assert not (self.session_token.query(Food_Types) is None)

        assert (food.food_type == "Italian2")
        assert (food.average_price == 3)
        assert (food.average_rating == 3)
        assert (food.image_url == "/food_types/italian/")
        assert (food.highest_rated_restaurant == 123)
        assert (food.best_location == 78787)

    def test_12_Food_Type_delete(self):
        
        '''
        Testing Deletion of Records on Food Types

        '''
        

        new_f=Food_Types(
                        food_type="Italian3",
                        average_price=3,
                        average_rating=3,
                        image_url="/food_types/italian/",
                        highest_rated_restaurant=123,
                        best_location=78787
                        )

        self.session_token.add(new_f)
        self.session_token.commit()

        f=self.session_token.query(Food_Types).filter_by(
            food_type="Italian3").first()

        self.session_token.delete(f)
        self.session_token.commit()

        f=self.session_token.query(Food_Types).filter_by(
            food_type="Italian3").first()

        assert (f is None)

    def test_13_restaurant_query_by_id(self):
        global session_token
        new_r1 = Restaurants(
                            name= "Little Italy16",
                            location=78701,
                            price=2,
                            rating=3,
                            hours="9 to 5",
                            food_type="Italian",
                            Recent_Review=1
                            )

        new_r2 = Restaurants(
                            name= "Not-So-Little Italy",
                            location=78701,
                            price=2,
                            rating=3,
                            hours="9 to 5",
                            food_type="Italian",
                            Recent_Review=1
                            )

        session_token.add(new_r1)
        session_token.commit()
        session_token.add(new_r2)
        session_token.commit()
        results = query_restaurant_by_id(session_token, 1)

        r = json.loads(results)

        assert(r is not None)
        assert(r["id"] == 1)

    def test_14_restaurant_query_all(self):
        global session_token
        results = query_all_restaurants(session_token)
        r = json.loads(results)

        assert(r is not None)
        assert(len(r) > 1)

    def test_15_location_query_by_zip(self):
        global session_token
        new_l=Locations(
                zipcode=77779,
                average_rating=3,
                average_price=2,
                adjacent_location=77778,
                average_health_rating=88,
                highest_price= 2,
                popular_food_type="Italian",
                highest_rated_restaurant="Little Italy17"
                )

        session_token.add(new_l)
        session_token.commit()

        result = query_location_by_zip(session_token, 77779)
        r = json.loads(result)
        assert (r is not None)
        assert (r["zipcode"] == 77779)

    def test_16_location_query_all(self) :
        global session_token
        results = query_all_locations(session_token)
        r = json.loads(results)
        assert (r is not None)
        assert (len(r) == 1)

    def test_17_food_type_query_by_name(self):
        global session_token
        new_f=Food_Types(
                        food_type="Chinese",
                        average_price=3,
                        average_rating=3,
                        country_of_origin="China",
                        image_url="/food_types/Chinese/",
                        open_restaurants=1,
                        highest_rated_restaurant=123,
                        best_location=78787
                        )

        session_token.add(new_f)
        session_token.commit()
        
        result = query_food_type_by_name(session_token, "Chinese")
        r = json.loads(result)

        assert (r is not None)
        assert (r["food_type"] == "Chinese")

    def test_18_food_type_query_all(self):
        global session_token
        results = query_all_food_types(session_token)
        r = json.loads(results)
        assert (r is not None)
        assert (len(r) > 0)

    def test_19_review_query_by_id(self):
        global session_token
        new_r=Reviews(
                    date="12/1/2014",
                    rating=5,
                    username="bob",
                    profile_picture_url="/review_profiles/pebs",
                    restaurant_pictures_url="/reviews_images/pebs/1",
                    restaurant_id=2,
                    zipcode=67778
                )

        session_token.add(new_r)
        session_token.commit()

        result = query_review_by_id(session_token, 1)
        r = json.loads(result)

        assert(r is not None)
        assert(r["review_id"] == 1)

    def test_20_review_query_all(self):
        global session_token
        results = query_all_reviews(session_token)
        r = json.loads(results)
        assert(r is not None)
        assert(len(r) > 0)
"""
# ----
# main
# ----

if __name__ == "__main__":  # pragma: no cover
    main()

