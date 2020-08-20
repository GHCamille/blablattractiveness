## Google Cloud Function 

import requests
import pandas as pd 
from google.cloud import storage
import datetime

def upload_blob(new_df):
    """Appends the new df to the csv in the bucket."""
    BUCKET_NAME = "blablattractivity"
    BLOB_NAME = "blablacar_rennes_brest.csv"

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(BUCKET_NAME)
    blob = bucket.blob(BLOB_NAME)
    assert blob.exists()  # Will be false if the next line would raise NotFound
    old_df = pd.read_csv('gs://'+BUCKET_NAME+'/'+BLOB_NAME,index_col = "Unnamed: 0")

    df_trips = old_df.append(new_df, ignore_index=True, sort=False)
    df_trips.to_csv('gs://'+BUCKET_NAME+'/'+BLOB_NAME)
  

def build_dataframe(api_url, api_token, from_coordinate, from_country, to_coordinate, to_country, locale, currency, number_of_trips_we_want_returned, start_date_local, radius_in_meters):
    """Builds the new dataframe to add to the one we have in our archives."""
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
    return new_df


def main(argument):
    # API setup
    api_token = open("./api.txt","r").read()
    api_url = "https://public-api.blablacar.com"
    from_coordinate = "48.117266%2C-1.677793" 
    to_coordinate = "48.390394%2C-4.486076" 
    from_country = "FR"
    to_country = "FR" 
    locale = "fr-FR" 
    currency = "EUR" 
    number_of_trips_we_want_returned = "100"  
    today = datetime.date.today()
    friday = today + datetime.timedelta( (4-today.weekday()) % 7 )
    next_friday_datetime = str(friday)+"T00:00:00"
    start_date_local = next_friday_datetime
    requested_seats = "1" 
    radius_in_meters = "6000" 

    new_df = build_dataframe(api_url, api_token, from_coordinate, from_country, to_coordinate, to_country, locale, currency, number_of_trips_we_want_returned, start_date_local, radius_in_meters)   
    upload_blob(new_df)
    
    return "OK"
