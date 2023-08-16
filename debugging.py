from flask import Flask, render_template, request
from utils import webscraper as ws
import pandas as pd
from opencage.geocoder import OpenCageGeocode
from datetime import datetime, timezone
from geopy import distance

location = "Bel Air, MD"

geocoder = OpenCageGeocode("b4733e5a94064bee8a2d0c1cded7f2b6")


df = pd.read_json(f'https://mass-shooting-tracker-data.s3.us-east-2.amazonaws.com/{datetime.now().year}-data.json')
candidates = []

today = datetime.now()

for i in df.index:
    if (today.replace(tzinfo=None) - (df['date'][i].to_pydatetime().replace(tzinfo=None))).days  < 30: 
        candidates.append(i)
    else:
        break

#calculate the distance
userinput = geocoder.geocode(location)

latA = userinput[0]['geometry']['lat']
lngA = userinput[0]['geometry']['lng']

curr = 9999
city = ''
state = ''
for i in candidates:
    result_B = geocoder.geocode(f'{df["city"][i]} {df["state"][i]}')
    latB = result_B[0]['geometry']['lat']
    lngB = result_B[0]['geometry']['lng']


    locations = {
    "shooting": (latB, lngB),
    "origin": (latA, lngA)
    }

    if distance.distance(locations['shooting'], locations['origin']).miles < curr:
        curr = distance.distance(locations['shooting'], locations['origin']).miles
        city = f'{df["city"][i]}'
        state = f'{df["state"][i]}'



print(curr, city, state)
