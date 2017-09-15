def decode_polyline(polyline_str):
    index, lat, lng = 0, 0, 0
    coordinates = []
    changes = {'latitude': 0, 'longitude': 0}

    # Coordinates have variable length when encoded, so just keep
    # track of whether we've hit the end of the string. In each
    # while loop iteration, a single coordinate is decoded.
    while index < len(polyline_str):
        # Gather lat/lon changes, store them in a dictionary to apply them later
        for unit in ['latitude', 'longitude']: 
            shift, result = 0, 0

            while True:
                byte = ord(polyline_str[index]) - 63
                index+=1
                result |= (byte & 0x1f) << shift
                shift += 5
                if not byte >= 0x20:
                    break

            if (result & 1):
                changes[unit] = ~(result >> 1)
            else:
                changes[unit] = (result >> 1)

        lat += changes['latitude']
        lng += changes['longitude']

        coordinates.append((lat / 100000.0, lng / 100000.0))

    return coordinates



'''import math
a1=18.6222681 #lat1
a2=18.5294062	#lat2
b1=73.86898029 #lon1
b2=73.8565749#lon2

d=2*math.asin(math.sqrt((math.sin((a2-a1)/2)*math.sin((a2-a1)/2))+math.cos(a1)*math.cos(a2)*math.sin((b2-b1)/2)*math.sin((b2-b1)/2)))
print d

# AIzaSyBk4pbCoAXVwI6A1aym14qST50eq4wqQyE
#Google maps geocoding api
'''


#AIzaSyA47CBshq2fOEMhtM15Mu7jj9QJ5O47YxU
#Distance matrix api

from googlemaps.client import Client
from googlemaps.distance_matrix import distance_matrix
api_key = 'AIzaSyA47CBshq2fOEMhtM15Mu7jj9QJ5O47YxU'
gmaps = Client(api_key)
distance = distance_matrix(gmaps, "gokul colony,dighi,pune,IN", "college of engineering,pune,IN","driving")
print(distance['rows'][0]['elements'][0]['distance']['text'])
print(distance['rows'][0]['elements'][0]['duration']['text'])
distance = distance_matrix(gmaps, "gokul+colony,+dighi,+pune,+IN", "college+of+engineering,+pune,+IN","walking")
print(distance['rows'][0]['elements'][0]['distance']['text'])
print(distance['rows'][0]['elements'][0]['duration']['text'])
distance = distance_matrix(gmaps, "gokul+colony,+dighi,+pune,+IN", "college+of+engineering,+pune,+IN","transit")
print(distance['rows'][0]['elements'][0]['distance']['text'])
print(distance['rows'][0]['elements'][0]['duration']['text'])
distance = distance_matrix(gmaps, "gokul+colony,+dighi,+pune,+IN", "college+of+engineering,+pune,+IN","bicycling")
'''if len(distance)>1:
    #print(distance['rows'][0]['elements'][0]['distance']['text'])
    #print(distance['rows'][0]['elements'][0]['duration']['text'])
else:
    print("bicycling route not available")
    '''
address = "gokul+colony,+dighi,+pune,+IN"
destination = "college+of+engineering,+pune,+IN"
directions = gmaps.directions(address, destination,"driving")
ans = []
ans=decode_polyline(str(directions))
#print(ans)
#print(directions['routes'][0]['legs'][0]['steps'])
