import os 
from dotenv import load_dotenv
from googlemaps import places
from googlemaps import client

#https://github.com/googlemaps/google-maps-services-python


load_dotenv()
google_places = places

def get_key ():
    MY_API_KEY = os.getenv('MY_API_KEY')
    return MY_API_KEY
key = get_key()

client_key = client.Client(key)

find_place = google_places.find_place(client_key, 
                                     "aldi", 
                                     "textquery" 
 )
print(find_place)
if find_place['status'] == 'OK' and find_place['candidates']:
    aldi_id = (find_place["candidates"][0]['place_id'])
print(aldi_id, )


aldi_info = google_places.place(client_key, aldi_id )
#print(aldi_info)

print(aldi_info["result"]["address_components"][0]["long_name"] ,": returned zip code , dict: dict: list : dict" )
print(aldi_info["result"]["formatted_address"])