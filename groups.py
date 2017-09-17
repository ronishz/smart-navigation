import json
import math
import os
f=open("final_location_data.json","r")
data=json.load(f)

def suggest_mode(two_wheeler_old,four_wheeler_old,bus_old,cab_old):
	s_mode = [[],[],[],[]]
	two_wheeler=len(two_wheeler_old)
	four_wheeler=len(four_wheeler_old)
	bus=len(bus_old)
	cab=len(cab_old)


	if(two_wheeler%2==0):
		s_mode[0].append(two_wheeler_old)
	elif(two_wheeler%2!=0):
		if(len(bus_old)>0):
			s_mode[0].append(two_wheeler_old)
			if(len(bus_old)==1):
				
				s_mode[0].append(list(bus_old))
		elif(len(cab_old)==1):
			s_mode[0].append(two_wheeler_old)
			
			s_mode[0].append(list(cab_old))
		else:
			s_mode[0].append(two_wheeler_old)
	
	if(four_wheeler==1  and cab==0):
		s_mode[2].append(four_wheeler_old)
	
	if(four_wheeler==0  and cab==1):
		s_mode[2].append(cab_old)

	if(four_wheeler+cab<=4):
		s_mode[1].append(four_wheeler_old)
		s_mode[1].append(cab_old)
	elif(four_wheeler<=4):
		 s_mode[1].append(four_wheeler_old)	

	if(cab>1 and four_wheeler==0):
		 s_mode[3].append(cab_old)		 
	


	return s_mode


def findGroupId(dist):
	if(dist<=34):
		for i in range(2,36,2):
			if(dist<=i):
				return i//2

	elif(dist>34):
		return 18	

def angle(lat2,lng2):
	lat1=18.531206
	lng1=73.855278
	#lat2=18.559128
	#lng2=73.827482
	y=math.sin(lng2-lng1)*math.cos(lat2)
	x=math.cos(lat1)*math.sin(lat2)-math.sin(lat1)*math.cos(lat2)*math.cos(lng2-lng1);
	brng=math.degrees(math.atan2(y,x))
	bearings=["NE", "E", "SE", "S", "SW", "W", "NW", "N"]
	index=brng-22.5
	if(index<0):
		index+=360
	index=int(index//45)
	return bearings[index]

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
	temp.update({'mode':"None"})
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
#print(grps)



for i in range(0,len(grps)):
		if(len(grps[i]))>=1:
			for j in range(len(grps[i])):
				temp_lat=0
				temp_lng=0
				temp_lat=data[(grps[i][j])-1]["latitude"]
				temp_lng=data[(grps[i][j])-1]["longitude"]
				dir1=angle(float(temp_lat),float(temp_lng))
				g[(grps[i][j])-1].update({'group_id':str(i+1)+dir1})



grps_new=[[[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[]]]
x=""
for i in range(len(g)):
	x=g[i]["group_id"]
	num=int(x[0])-1
	if(x[1:]=="N"):
		num1=0
	elif(x[1:]=="S"):
		num1=1
	elif(x[1:]=="E"):
		num1=2
	elif(x[1:]=="W"):
		num1=3
	elif(x[1:]=="NW"):
		num1=4
	elif(x[1:]=="NE"):
		num1=5
	elif(x[1:]=="SW"):
		num1=6
	elif(x[1:]=="SE"):
		num1=7						
			
	grps_new[num][num1].append(g[i]["user_id"])

print(grps_new)

for i in range(0,len(grps_new)):
		for j in range(len(grps_new[i])):
			if(len(grps_new[i]))>=1:
				max_d=0
				start_id1=0
				for k in range(len(grps_new[i][j])):
					if(len(grps_new[i][j]))>=1:
						temp_max=float((data[(grps_new[i][j][k])-1]["distance1"]).split()[0])
						temp_start_id=grps_new[i][j][k]
						if((temp_max)>float(max_d)):
							max_d=temp_max
							start_id1=temp_start_id
				
				for k in range(len(grps_new[i][j])):
					if(len(grps_new[i][j]))>=1:
						g[(grps_new[i][j][k])-1].update({'start_id':start_id1})





for i in range(0,len(grps_new)):
	if(len(grps_new[i])>=1):		
		for j in range(len(grps_new[i])):
			
				two_wheeler=0
				four_wheeler=0
				bus=0
				cab=0
				cab_old =  []
				two_wheeler_old = []
				four_wheeler_old = []
				bus_old = []
				if(len(grps_new[i][j])>=1):
					for k in range(len(grps_new[i][j])):
						
							if(data[(grps_new[i][j][k])-1]["mode"]=='2w'):
								two_wheeler+=1
								two_wheeler_old.append((grps_new[i][j][k])-1)
							elif(data[(grps_new[i][j][k])-1]["mode"]=='4w'):
								four_wheeler+=1
								four_wheeler_old.append((grps_new[i][j][k])-1)
							elif(data[(grps_new[i][j][k])-1]["mode"]=='bus'):
								bus+=1
								bus_old.append((grps_new[i][j][k])-1)
							elif(data[(grps_new[i][j][k])-1]["mode"]=='cab'):
								cab+=1
								cab_old.append((grps_new[i][j][k])-1)

				
				'''for i in range(0,len(g)):
					g[i].update({'mode':data[i]['mode']})
'''
				s_mode = []
				s_mode=suggest_mode(two_wheeler_old,four_wheeler_old,bus_old,cab_old)
				for x in range(0,4):
					for y in range(0,len(s_mode[x])):
						for z in range(0,len(s_mode[x][y])):
							if(x==0):
								g[(s_mode[x][y][z])-1].update({'mode':'2w_shared'})
							elif(x==1):
								g[(s_mode[x][y][z])-1].update({'mode':'4w_shared'})
							elif(x==2):
								g[(s_mode[x][y][z])-1].update({'mode':'bus'})
							elif(x==3):
								g[(s_mode[x][y][z])-1].update({'mode':'cab_shared'})

												

				

print(g)





#print(g)
'''
check=[]
for i in range(len(g)):
	check.append(g[i]["group_id"])
check.sort()
	'''
#print(check)
#print(data[grps[2][13]]["latitude"])	
#print(len(grps[16]))

for i in range(0,len(g)):
	data[i].update({'group_id':g[i]['group_id']})


for i in range(0,len(g)):
	try:
		data[i].update({'start_id':g[i]['start_id']})	
	except KeyError:
		pass

	

for i in range(0,len(g)):
	try:
		data[i].update({'mode':g[i]['mode']})	
	except KeyError:
		pass


f1=open("start_location_data.json","w")
json.dump(data,f1)


	
