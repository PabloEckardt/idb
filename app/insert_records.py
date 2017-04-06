# import our models
from models import Restaurants, Locations, Food_Types, Reviews, Base



def add_restaurant(session_obj,
                   id,
                   name,
                   yelp_id,
                   location,
                   lat,
                   long,
                   city,
                   address,
                   phone,
                   price,
                   rating,
                   review,
                   review_date,
                   review_count,
                   url,
                   img_url,
                   *food_types):


    new_restaurant = Restaurants(
                                id=id,
                                name=name,
                                yelp_id=yelp_id,
                                location=location,
                                lat=lat,
                                long=long,
                                city=city,
                                address=address,
                                phone=phone,
                                price=price,
                                rating=rating,
                                review=review,
                                review_date=review_date,
                                review_count=review_count,
                                url=url,
                                img_url=img_url,
                                food_type=food_types[0],
                                food_type2=food_types[1],
                                food_type3=food_types[2]
                                )

    session_obj.add(new_restaurant)
    session_obj.commit()


def add_location(session_obj, average_rating, average_price,
                zipcode, highest_price, popular_food_type, highest_rated_restaurant):

    new_location = Locations(
        average_rating=average_rating,
        average_price=average_price,
        zipcode=zipcode,
        highest_price=highest_price,
        popular_food_type=popular_food_type,
        highest_rated_restaurant=highest_rated_restaurant
    )

    session_obj.add(new_location)
    session_obj.commit()


def add_food_type(session_obj,
                  food_type,
                  average_price,
                  average_rating,
                  image_url,
                  highest_rated_restaurant,
                  best_location,):

    new_food_type = Food_Types(
        food_type=food_type,
        average_price=average_price,
        average_rating=average_rating,
        image_url=image_url,
        highest_rated_restaurant=highest_rated_restaurant,
        best_location=best_location
    )

    session_obj.add(new_food_type)
    session_obj.commit()


def add_review(
                session_obj,
                restaurant_id,
                yelp_restaurant_id,
                date,
                rating,
                username,
                review,
                profile_picture_url,
                review_url,
                zipcode
               ):

    # I realized that having zipcode and restaurant id is wasteful.
    new_review = Reviews(
        restaurant_id=restaurant_id,
        yelp_restaurant_id=yelp_restaurant_id,
        date=date,
        rating=rating,
        username=username,
        review=review,
        profile_picture_url=profile_picture_url,
        review_url=review_url,
        zipcode=zipcode
    )

    session_obj.add(new_review)
    session_obj.commit()
