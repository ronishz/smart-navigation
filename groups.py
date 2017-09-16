import json
f=open("final_location_data.json","r")
data=json.load(f)

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
temp_g=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(len(g)):
	x=g[i]["group_id"]
	x-=1
	temp_g[x]+=1
print(temp_g)




	
	
