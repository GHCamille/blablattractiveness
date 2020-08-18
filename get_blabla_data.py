# Imports

import json
import requests
import pandas as pd

# API setup
api_token = open("./api/api.txt","r").read()
api_url = "https://public-api.blablacar.com"

from_coordinate = "48.117266%2C-1.677793" 
to_coordinate = "48.390394%2C-4.486076" 
from_country = "FR"
to_country = "FR" 
locale = "fr-FR" 
currency = "EUR" 
number_of_trips_we_want_returned = "100"  
start_date_local = "2020-08-21T17:00:00" 
requested_seats = "1" 
radius_in_meters = "6000" 

# REQUEST
response = requests.get(api_url+"/api/v3/trips?key="+api_token+"&from_coordinate="+from_coordinate+"&from_country="
                        +from_country+"&to_coordinate="+to_coordinate+"&to_country="+to_country+"&locale="
                        +locale+"&currency="+currency+"&count="+number_of_trips_we_want_returned+"&start_date_local="
                        +start_date_local+"&radius_in_meters="+radius_in_meters+"&sort=price:asc") 

# DICTIONNARY
json_trips = response.json()
new_dict = {'trip_id':[],'price_of_the_trip':[],'date':[]} # good to keep the date easy to access
for dict_trip in json_trips["trips"]:
    trip_id =  dict_trip["link"].split("id=")[1].split("-")[0]
    price_of_the_trip = dict_trip["price"]["amount"]
    new_dict['trip_id'].append(trip_id)
    new_dict['price_of_the_trip'].append(price_of_the_trip)
    new_dict['date'].append(start_date_local[:10])

# DATAFRAME
new_df = pd.DataFrame.from_dict(new_dict)

old_df = pd.read_csv("./blablacar_rennes_brest.csv",index_col = "Unnamed: 0")

df_trips = old_df.append(new_df, ignore_index=True, sort=False)
df_trips.to_csv("./blablacar_rennes_brest.csv")