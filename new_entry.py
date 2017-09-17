import json
import random
import geocoder

from googlemaps.client import Client
from googlemaps.distance_matrix import distance_matrix
api_key = 'AIzaSyA47CBshq2fOEMhtM15Mu7jj9QJ5O47YxU'
gmaps = Client(api_key)

add=input()
temp_mode=input()


g=geocoder.google(str(add)+"pune,IN")
lat=float(g.latlng[0])
lng=float(g.latlng[1])


print("Latitude:	"+str(lat))
print("Longitude:	"+str(lng))

if(temp_mode=='2w' or temp_mode=='4w' or temp_mode=='cab' ):
		distance2 = distance_matrix(gmaps, str(add)+",pune,IN", "college of engineering,pune,IN","driving")
		print(distance2['rows'][0]['elements'][0]['distance']['text'])
		print(distance2['rows'][0]['elements'][0]['duration']['text'])
elif(temp_mode=='bus'):
		distance2 = distance_matrix(gmaps, str(add)+",pune,IN", "college of engineering,pune,IN","transit")
		print(distance2['rows'][0]['elements'][0]['distance']['text'])
		print(distance2['rows'][0]['elements'][0]['duration']['text'])
