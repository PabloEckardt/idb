"""
This file contains all of the configuration values for the application.
Update this file with the values for your specific Google Cloud project.
You can create and manage projects at https://console.developers.google.com
"""

import os

# The secret key is used by Flask to encrypt session cookies.
SECRET_KEY = 'secret'

# Google Cloud Project ID. This can be found on the 'Overview' page at
# https://console.developers.google.com
PROJECT_ID = 'foodclosetome-162203'

SQLALCHEMY_DATABASE = 'sqlite:///app/db/food_close_to.db'

RESTAURANTS = 'app/db/restaurants.json'

LOCATIONS = 'app/db/locations.json'

FOOD_TYPES = 'app/db/food_types.json'

REVIEWS = 'app/db/reviews.json'
