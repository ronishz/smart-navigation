import geocoder
g=geocoder.google("pune,IN")
g1=g.bbox
lat1=float(g1['northeast'][0])
lat2=float(g1['southwest'][0])

lng1=float(g1['northeast'][1])
lng2=float(g1['southwest'][1])

print(lat1)
print(lat2)

print(lng1)
print(lng2)

diff_lat=lat1-lat2
diff_lng=lng1-lng2      

d1=(lat1-lat2)/5
d2=(lng1-lng2)/5


lat = []
lng = []

lat.append(lat1)
lng.append(lng2)
for i in range(1,6):
    lat.append(lat1-d1*i)
    lng.append(lng2+d2*i)
print(lat)
print(lng)


lat_find=float(input("Enter lat_find:   "))
lng_find=float(input("Enter lng_find:   "))

flag=1
for i in range(len(lat)):
    if(lat_find<lat[i]):
        flag=1
    else:
        #print(lat[i])
        lat_v=i
        break
 
flag=1 
for i in range(len(lng)):
    if(lng_find>lng[i]):
        flag=1
    else:
        #print(lng[i])
        lng_v=i
        break

blk=lng_v+(lat_v-1)*5        
print(lat_v)
print(lng_v)
print("blk= "+str(blk))
 
        
