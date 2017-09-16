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
#print(g)
'''
temp_g=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
'''
grps=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
for i in range(len(g)):
	x=g[i]["group_id"]
	x-=1
	grps[x].append(g[i]["user_id"])
print(grps)
'''
temp=[]
for i in range(0,len(grps)):
		#temp=grps[i]
		if(len(grps[i]))>1:
			for j in range(len(grps[i])):
				temp_lat=0
				temp_lng=0
				temp_lat=data[grps[i][j]]["latitude"]
				temp_lng=data[grps[i][j]]["longitude"]
				print(temp_lat)
				print(temp_lng)
'''
print(data[grps[17][0]]["latitude"])	
	
