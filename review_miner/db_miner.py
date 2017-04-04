# -*- coding: utf-8 -*-
"""
Yelp Fusion API code sample without the superflous data.

This program demonstrates the capability of the Yelp Fusion API
by using the Search API to query for businesses by a search term and location,
and the Business API to query additional information about the top result
from the search query.

Please refer to http://www.yelp.com/developers/v3/documentation for the API
documentation.

This program requires the Python requests library, which you can install via:
`pip install -r requirements.txt`.

Sample usage of the program:
`python sample.py --term="bars" --location="San Francisco, CA"`
"""
from __future__ import print_function

import argparse
import json
import pprint
import requests
import sys
import urllib


# This client code can run on Python 2.x or 3.x.  Your imports can be
# simpler if you only need one of those.
try:
    # For Python 3.0 and later
    from urllib.error import HTTPError
    from urllib.parse import quote
    from urllib.parse import urlencode
except ImportError:
    # Fall back to Python 2's urllib2 and urllib
    from urllib2 import HTTPError
    from urllib import quote
    from urllib import urlencode


# OAuth credential placeholders that must be filled in by users.
# You can find them on
# https://www.yelp.com/developers/v3/manage_app
CLIENT_ID = "oQeTOrWw-rVtEKjG6sA2ew"
CLIENT_SECRET = "8wZGatI4Bjq064mYOa37QdmYvO3VdeJsoq6Ju7kaASPP9nhS2FmRKnAR4NZcg7BM"


# API constants, you shouldn't have to change these.
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.
TOKEN_PATH = '/oauth2/token'
GRANT_TYPE = 'client_credentials'


# Defaults for our simple example.
DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = 'San Francisco, CA'
SEARCH_LIMIT = 50


def obtain_bearer_token(host, path):
    """Given a bearer token, send a GET request to the API.

    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        url_params (dict): An optional set of query parameters in the request.

    Returns:
        str: OAuth bearer token, obtained using client_id and client_secret.

    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    assert CLIENT_ID, "Please supply your client_id."
    assert CLIENT_SECRET, "Please supply your client_secret."
    data = urlencode({
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': GRANT_TYPE,
    })
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
    }
    response = requests.request('POST', url, data=data, headers=headers)
    bearer_token = response.json()['access_token']
    return bearer_token



def main():

    bearer_token = obtain_bearer_token(API_HOST, TOKEN_PATH)

    headers = {
        'Authorization': 'Bearer %s' % bearer_token,
    }

    reviews = {}
    reviews_collected = []
    reviews_not_collected = []

    count = 0
    with open ("new_mega.json", "r") as m:
        new_mega = json.load(m)
        for key in new_mega:
            print(count)
            count += 1
            id = new_mega[key]["id"]
            url = "https://api.yelp.com/v3/businesses/" + id + "/reviews"
            response = requests.request('GET', url, headers=headers)
            if not response:
                reviews_not_collected.append(key)
                print("key:", key,"is broken")
            else:
                reviews[key] = response.json().get("reviews")
                reviews_collected.append(key)
                if count == 10:
                    break


    with open ("review_key_data.txt") as rkd:
        rkd.write("collected")
        for c in reviews_collected:
            rkd.write(c,"\n")
        rkd.write("not collected")
        for c in reviews_not_collected:
            rkd.write(c,"\n")

    with open ("reviews.json", "w") as r:
        json.dump(reviews, r, indent=4)

if __name__ == '__main__':
    main()
