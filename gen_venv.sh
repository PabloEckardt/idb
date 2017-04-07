#!/bin/sh
# Create virtualenv
virtualenv -p python3 venv
# Source it
. ./venv/bin/activate
# Install requirements for the virtualenv
pip install -r requirements.txt
