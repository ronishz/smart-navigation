import json
f=open("final_location_data.json","r")
data=json.load(f)
data=data["dB"]
#print(data[0])

def findGroupId(dist):
	if(dist<=34):
		for i in range(2,36,2):
			if(dist<=i):
				return i//2

	elif(dist>34):
		return 18			


def findDirection(lat,lng):
	dest_lat=18.531206
	dest_lng=73.855278
	if((abs(lat-dest_lat)>abs(lng-dest_lng)) and lat>dest_lat):
		return "N"
	elif((abs(lat-dest_lat)>abs(lng-dest_lng)) and lat<dest_lat):
		return "S"
	elif((abs(lng-dest_lng)>abs(lat-dest_lat)) and lng<dest_lng):
		return "W"
	elif((abs(lng-dest_lng)>abs(lat-dest_lat)) and lng>dest_lng):
		return "E"	





g = []
for i in range(0,len(data)):
	temp={}
	temp_dist=float(str(data[i]["distance1"]).split()[0])
	

	#print(findGroupId(temp_dist))
	#g.append(findGroupId(temp_dist))
	#print(set(g))
	
	temp.update({'group_id':findGroupId(temp_dist)})
	temp.update({'user_id':i+1})
	g.append(temp)
print(g)
'''
temp_g=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
'''
grps=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
for i in range(len(g)):
	x=g[i]["group_id"]
	x-=1
	grps[x].append(g[i]["user_id"])
print(grps)



for i in range(0,len(grps)):
		if(len(grps[i]))>=1:
			for j in range(len(grps[i])):
				temp_lat=0
				temp_lng=0
				temp_lat=data[(grps[i][j])-1]["latitude"]
				temp_lng=data[(grps[i][j])-1]["longitude"]

				dir1=findDirection(float(temp_lat),float(temp_lng))
				g[(grps[i][j])-1].update({'group_id':str(i+1)+dir1})
				
				#print(temp_lat)
				#print(temp_lng)
print(g)
#print(data[grps[2][13]]["latitude"])	
#print(len(grps[16]))
	
