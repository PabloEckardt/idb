#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = bad-continuation
# pylint: disable = superfluous-parens
# pylint: disable = import-error
# -------
# imports
# -------
from unittest import main, TestCase
import os
from models import Restaurants, Locations, Food_Types, Reviews
from insert_records import add_restaurant, add_location, add_food_type, add_review
from db_manager import setupdb, init_session, create_engine


class test_db (TestCase):

    session_token = None

    def setUp(self):
        if os.path.isfile("testdb.db"):
            os.remove("testdb.db")

        db_name = 'sqlite:///testdb.db'
        testEngine = create_engine(db_name)
        setupdb(testEngine)
        Session = init_session(testEngine)
        session_token = Session()
        self.session_token = session_token

    def test_1_restaurant_addition(self):
        '''
        Testing our Wrapper to add records on Restaurants

        '''
        food_types = ["hot_pot", None, None, "Hot Pot", None, None]
        add_restaurant(
            self.session_token,
            u"0001",
            u"Little Italy",
            u"little_italy",
            78701,
            1.0000,
            1.0000,
            u"Austin",
            u"123 f",
            u"(512)123123",
            u"$",
            3.0,
            u"test_review",
            u"Today",
            123,
            u"www.web.com",
            u"www.web.com/img.jpg",
            *food_types
        )

        assert not (self.session_token.query(Restaurants) is None)
        print ("Passed Test1")

    def test_2_Restaurants_manual_integrity(self):
        '''
        Testing query data on Restaurants
        '''
        food_types = ["Italian", "Italian", None, None, None, None]
        new_r = Restaurants(
            u"0002",
            u"Little Italy2",
            u"little_italy",
            78701,
            1.0000,
            1.0000,
            u"Austin",
            u"123 f",
            u"(512)123123",
            u"$",
            3.0,
            u"test_review",
            u"Today",
            123,
            u"www.web.com",
            u"www.web.com/img.jpg",
            *food_types
        )

        self.session_token.add(new_r)
        self.session_token.commit()

        restaurant_1 = self.session_token.query(Restaurants).filter_by(
            name="Little Italy2").first()

        # test serialize
        assert (isinstance(restaurant_1.to_dict(), dict))

        # test data types
        assert not (self.session_token.query(Restaurants) is None)
        assert restaurant_1.id == "0002"
        assert restaurant_1.name == "Little Italy2"
        assert restaurant_1.location == 78701
        assert restaurant_1.lat == 1.0000
        assert restaurant_1.long == 1.0000
        assert restaurant_1.city == "Austin"
        assert restaurant_1.price == "$"
        assert restaurant_1.rating == 3.0
        assert restaurant_1.food_type == "Italian"
        assert restaurant_1.review == "test_review"
        assert restaurant_1.review_date == "Today"
        print("Passed Test2")

    def test_3_Restaurants_delete(self):
        '''
        Testing Deletion of Records on Restaurants

        '''

        food_types = ["Italian", "Italian", None, None, None, None]
        new_r = Restaurants(
            u"0003",
            u"Little Italy 3",
            u"little_italy",
            78701,
            1.0000,
            1.0000,
            u"Austin",
            u"123 f",
            u"(512)123123",
            u"$",
            3.0,
            u"test_review",
            u"Today",
            123,
            u"www.web.com",
            u"www.web.com/img.jpg",
            *food_types
        )

        self.session_token.add(new_r)
        self.session_token.commit()

        rst = self.session_token.query(Restaurants).filter_by(
            name="Little Italy 3").first()

        self.session_token.delete(rst)
        self.session_token.commit()

        rst = self.session_token.query(Restaurants).filter_by(
            name="Little Italy 3").first()

        assert (rst is None)
        print("Passed Test3")

    def test_4_Locations_addition(self):
        '''
        Testing our Wrapper to add records on Locations

        '''
        add_location(
            self.session_token,
            "00001",
            3.0,
            3.0,
            "$$$$",
            "$",
            "Italian",  # popular food type
            "Little Italy",  # highest rated restaurant
            "Pizza Joint",  # most popular restaurant
            40
        )

        assert not (self.session_token.query(Locations) is None)
        print("Passed Test4")

    def test_5_Locations_manual_integrity(self):
        '''
        Testing query data on Locations

        '''

        new_l = Locations(
            "00002",  # zip
            3.0,  # avg rate
            3.0,  # avg price
            "$$$$",  # high price
            "$",  # low price
            "Italian",  # popular food type
            "Little Italy",  # highest rated restaurant
            "Pizza Joint",  # most popular restaurant
            40  # number restaurants
        )

        self.session_token.add(new_l)
        self.session_token.commit()

        loc = self.session_token.query(
            Locations).filter_by(zipcode="00002").first()

        assert not (self.session_token.query(Locations) is None)

        # test serialize
        assert isinstance(loc.to_dict(), dict)

        # test query
        assert (loc.zipcode == "00002")
        assert (loc.average_rating == 3.0)
        assert (loc.average_price == 3.0)
        assert (loc.highest_price == "$$$$")
        assert (loc.popular_food_type == "Italian")
        assert (loc.highest_rated_restaurant == "Little Italy")
        print("Passed Test5")

    def test_6_Locations_delete(self):
        '''
        Testing Deletion of Records on Locations

        '''

        new_l = Locations(
            "00003",  # zip
            3.0,  # avg rate
            3.0,  # avg price
            "$$$$",  # high price
            "$",  # low price
            "Italian",  # popular food type
            "Little Italy",  # highest rated restaurant
            "Pizza Joint",  # most popular restaurant
            40  # number restaurants
        )

        self.session_token.add(new_l)
        self.session_token.commit()

        l = self.session_token.query(
            Locations).filter_by(zipcode="00003").first()

        self.session_token.delete(l)
        self.session_token.commit()

        l = self.session_token.query(
            Locations).filter_by(zipcode="00003").first()

        assert (l is None)
        print("Passed Test6")

    def test_7_Reviews_addition(self):
        '''
        Testing our Wrapper to add records on Reviews

        '''
        add_review(
            self.session_token,
            u"001",
            u"Little Italy",
            u"yelp_italy",
            u"italian",
            u"Italian",
            u"12/1/2014",
            4,
            u"pebs",
            u"pretty good",
            u"/review_profiles/pebs",
            u"/review/1",
            u"002",
        )

        assert not (self.session_token.query(Reviews) is None)
        print("Passed Test7")

    def test_8_Reviews__manual_integrity(self):
        '''
        Testing query data on Reviews

        '''

        new_r = Reviews(
            u"009",  # rest id
            u"Little_Italy",  # name
            u"italy",  # yelp id
            u"italian",
            u"Italian",
            u"12/1/2014",  # date
            4,  # rating
            u"pebs",  # username
                u"pretty good",  # review
                u"/review_profiles/pebs",  # img url
                u"/review/1",  # rev url
                u"002",  # zip
        )

        self.session_token.add(new_r)
        self.session_token.commit()

        rev = self.session_token.query(Reviews).filter_by(
            restaurant_id=u"009").first()

        assert not (self.session_token.query(Reviews) is None)

        # test serialize
        assert isinstance(rev.to_dict(), dict)

        # test query
        assert (rev.date == u"12/1/2014")
        assert (rev.rating == 4)
        assert (rev.username == u"pebs")
        assert (rev.profile_picture_url == u"/review_profiles/pebs")
        assert (rev.review_url == u"/review/1")
        assert (rev.restaurant_id == u"009")
        print("Passed Test8")

    def test_9_Reviews_delete(self):
        '''
        Testing Deletion of Records on Reviews

        '''

        new_r = Reviews(
            u"0010",  # rest id
            u"Little_Italy",  # name
            u"italy",  # yelp id
            u"italian",
            u"Italian",
            u"12/1/2014",  # date
            4,  # rating
            u"pebs",  # username
                u"pretty good",  # review
                u"/review_profiles/pebs",  # img url
                u"/review/1",  # rev url
                u"002",  # zip
        )

        self.session_token.add(new_r)
        self.session_token.commit()

        r = self.session_token.query(Reviews).filter_by(
            restaurant_id=u"0010").first()

        self.session_token.delete(r)
        self.session_token.commit()

        r = self.session_token.query(Reviews).filter_by(
            restaurant_id=u"0010").first()

        assert (r is None)
        print("Passed Test9")

    def test_10_Food_Type_addition(self):
        '''
        Testing our Wrapper to add records on Food Types

        '''

        add_food_type(
            self.session_token,
            u"Italianese",
            u"Italianese =]",
            3.0,
            3.0,
            u"/food_types/italian/img.jpg",
            100,
            u"Little Italy",
            u"Large Italy",
            u"00001"
        )

        assert not (self.session_token.query(Food_Types) is None)
        print("Passed Test10")

    def test_11_Food_Type_manual_Integrity(self):
        '''
        Testing query data on Food Types

        '''

        new_f = Food_Types(
            u"Italian",
            u"Italian =]",
            3.0,
            3.0,
            u"/food_types/italian/img.jpg",
            100,
            u"Little Italy",
            u"Large Italy",
            u"00001"
        )

        self.session_token.add(new_f)
        self.session_token.commit()

        food = self.session_token.query(Food_Types).filter_by(
            food_type=u"Italian").first()

        assert not (self.session_token.query(Food_Types) is None)

        # test serialize
        assert isinstance(food.to_dict(), dict)

        # test query
        assert (food.food_type == u"Italian")
        assert (food.average_price == 3.0)
        assert (food.average_rating == 3.0)
        assert (food.image_url == u"/food_types/italian/img.jpg")
        assert (food.highest_rated_restaurant == u"Large Italy")
        assert (food.best_location == u"00001")
        print("Passed Test11")

    def test_12_Food_Type_delete(self):
        '''
        Testing Deletion of Records on Food Types

        '''

        new_f = Food_Types(
            u"French",
            u"French!",
            3.0,
            3.0,
            u"/food_types/fre/img.jpg",
            100,
            u"Little france",
            u"Large france",
            u"00001"
        )

        self.session_token.add(new_f)
        self.session_token.commit()

        f = self.session_token.query(Food_Types).filter_by(
            food_type=u"French").first()

        self.session_token.delete(f)
        self.session_token.commit()

        f = self.session_token.query(Food_Types).filter_by(
            food_type=u"French").first()

        assert f is None
        print("Passed Test12")


if __name__ == "__main__":  # pragma: no cover
    main()
