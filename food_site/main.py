import os 
from dotenv import load_dotenv
from googlemaps import places
from googlemaps import client
import pandas as pd

#https://github.com/googlemaps/google-maps-services-python


load_dotenv()
google_places = places

def get_key ():
    MY_API_KEY = os.getenv('MY_API_KEY')
    return MY_API_KEY
key = get_key()

client_key = client.Client(key)


user_location = input("what location are you looking for: ? ")
def find_location(user_location, ):
    found_location = google_places.find_place(client_key, user_location, "textquery")    

    return found_location

found_location = find_location(user_location)




 
print(found_location)
if found_location['status'] == 'OK' and found_location['candidates']:
    location_id = (found_location["candidates"][0]['place_id'])
print(location_id, )


location_info = google_places.place(client_key, location_id )

#test prints
#print(location_info["result"]["address_components"][0]["long_name"] ,": returned zip code , dict: dict: list : dict" )
#print(location_info["result"]["formatted_address"])
#print(location_info)

# start of panda
pd_location_info = pd.json_normalize(location_info["result"]['address_components'])
print(pd_location_info)