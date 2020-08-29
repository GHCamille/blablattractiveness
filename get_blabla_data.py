import requests
import pandas as pd 
from google.cloud import storage
import datetime

def api_connection():
    # API setup
    api_token = open("./api.txt","r").read()
    api_url = "https://public-api.blablacar.com"
    return api_token, api_url

def setup_parameters():
    from_country = "FR"
    to_country = "FR" 
    locale = "fr-FR" 
    currency = "EUR" 
    number_of_trips_we_want_returned = "100" # it's the maximum value  
    requested_seats = "1" 
    radius_in_meters = "6000" 
    return from_country, to_country, locale, currency, number_of_trips_we_want_returned, requested_seats, radius_in_meters

def get_next_friday():
    today = datetime.date.today()
    friday = today + datetime.timedelta( (4-today.weekday()) % 7 )
    next_friday_datetime = str(friday)+"T00:00:00"
    return next_friday_datetime

def connect_to_bucket(bucket_name, blob_name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    assert blob.exists()  # Will be false if the next line would raise NotFound
    result = blob.download_as_string()
    return result

def route_info(route_dict, index):
        current_origin = route_dict[index]['Origin']
        current_destination = route_dict[index]['Destination']
        from_coordinate = route_dict[index]['From_coordinate'] # string : latitude, longitude - current_origin
        to_coordinate = route_dict[index]['To_coordinate'] # string : latitude, longitude - current_destination
        distance = route_dict[index]['Distance']
        return current_origin, current_destination, from_coordinate, to_coordinate, distance

def hello_world(argument):

    BUCKET_NAME = "blablattractivity_2"
    BLOB_INFO_NAME = "origin_destination.csv"
    BLOB_DF_NAME = "blabla_df.csv"

    # Get all parameters value
    api_token, api_url = api_connection()
    from_country, to_country, locale, currency, number_of_trips_we_want_returned, requested_seats, radius_in_meters = setup_parameters()

    # Setup date
    start_date_local = get_next_friday()
     

    result = connect_to_bucket(BUCKET_NAME, BLOB_INFO_NAME)
    origin_destination_df = pd.read_csv('gs://'+BUCKET_NAME+'/'+BLOB_INFO_NAME, sep=";") # index_col = "Unnamed: 0"
    route_dict = origin_destination_df.to_dict('index')
    new_dict = {'trip_id':[],'price_of_the_trip':[],'date':[],'origin':[],'destination':[],'count_trips_on_this_route':[],'distance':[]}  # Create the dictionnary that is going to hold our information


    # REQUEST
    for index in route_dict:
        current_origin, current_destination, from_coordinate, to_coordinate, distance = route_info(route_dict, index)
        blabla_query = api_url+"/api/v3/trips?key="+api_token+"&from_coordinate="+from_coordinate+"&from_country="+from_country+"&to_coordinate="+to_coordinate+"&to_country="+to_country+"&locale="+locale+"&currency="+currency+"&count="+number_of_trips_we_want_returned+"&start_date_local="+start_date_local+"&radius_in_meters="+radius_in_meters+"&sort=price:asc"
        response = requests.get(blabla_query) # print(response.status_code) # SHOULD BE 200
        json_trips = response.json() # it's a dictionnary
    
        try:
            print(json_trips)
            number_of_trips = json_trips["search_info"]["count"]
            for dict_trip in json_trips["trips"]:
                trip_id =  dict_trip["link"].split("id=")[1].split("-")[0]
                price_of_the_trip = dict_trip["price"]["amount"]
                new_dict['trip_id'].append(trip_id)
                new_dict['price_of_the_trip'].append(price_of_the_trip)
                new_dict['date'].append(start_date_local[:10])
                new_dict['origin'].append(current_origin)
                new_dict['destination'].append(current_destination)
                new_dict['count_trips_on_this_route'].append(number_of_trips)
                new_dict['distance'].append(distance)
        except:
            print("Unexpected error.")

    # DATAFRAME
    new_df = pd.DataFrame.from_dict(new_dict)
    new_df.price_of_the_trip = new_df.price_of_the_trip.astype('float')

    result = connect_to_bucket(BUCKET_NAME, BLOB_DF_NAME)
    old_df = pd.read_csv('gs://'+BUCKET_NAME+'/'+BLOB_DF_NAME,index_col = "Unnamed: 0")

    df_trips = old_df.append(new_df, ignore_index=True, sort=False)
    df_trips.to_csv('gs://'+BUCKET_NAME+'/'+BLOB_DF_NAME)
    return "OK"
