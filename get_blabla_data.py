# Imports

import json
import requests
import pandas as pd

# API setup
api_token = open("./api/api.txt","r").read()
api_url = "https://public-api.blablacar.com"

from_coordinate = "48.117266%2C-1.677793" # string : latitude, longitude - RENNES
to_coordinate = "48.390394%2C-4.486076" # string : latitude, longitude - BREST
from_country = "FR" # string : ISO_3166_1
to_country = "FR" # string : ISO_3166_1
locale = "fr-FR" # string : locale in which the result will be displayed 
                 #https://dev.blablacar.com/hc/en-us/articles/360008930020
currency = "EUR" # string : ISO_4217 currency
number_of_trips_we_want_returned = "100" # int : from 1 to 100, default is 10 
start_date_local = "2020-08-21T17:00:00" # string(date-time) : Format: "yyyy-M-dTHH:mm:ss"
requested_seats = "1" # int : minimum number of seats requested, default value is 1
radius_in_meters = "6000" # int : radius of the circle around the coordinates in which trips will be searched 
                          # from (in meters)

response = requests.get(api_url+"/api/v3/trips?key="+api_token+"&from_coordinate="+from_coordinate+"&from_country="
                        +from_country+"&to_coordinate="+to_coordinate+"&to_country="+to_country+"&locale="
                        +locale+"&currency="+currency+"&count="+number_of_trips_we_want_returned+"&start_date_local="
                        +start_date_local+"&radius_in_meters="+radius_in_meters+"&sort=price:asc") 

# DICTIONNARY
json_trips = response.json() # it's a dictionnary
new_dict = {'trip_id':[],'price_of_the_trip':[]}
for dict_trip in json_trips["trips"]:
    trip_id =  dict_trip["link"].split("id=")[1].split("-")[0]
    #number_of_passenger =  dict_trip["link"].split("id=")[1].split("-")[0]
    price_of_the_trip = dict_trip["price"]["amount"]
    new_dict['trip_id'].append(trip_id)
    new_dict['price_of_the_trip'].append(price_of_the_trip)

# DATAFRAME
df_trips = pd.DataFrame.from_dict(new_dict)
df_trips.head()