from flask import Flask, render_template, request
from utils import webscraper as ws
import pandas as pd
from opencage.geocoder import OpenCageGeocode
from datetime import datetime, timezone
from geopy.distance import geodesic
from utils import webscraper


geocoder = OpenCageGeocode("b4733e5a94064bee8a2d0c1cded7f2b6")
geo = geocoder.geocode("michigan, va", countrycode = 'us')


latA = geo[0]['geometry']['lat']
lngA = geo[0]['geometry']['lng']
print(latA, lngA)



