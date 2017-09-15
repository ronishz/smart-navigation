import json
import random

from googlemaps.client import Client
from googlemaps.distance_matrix import distance_matrix
api_key = 'AIzaSyA47CBshq2fOEMhtM15Mu7jj9QJ5O47YxU'
gmaps = Client(api_key)



a=[{"location_id":"387","zone_id":"11","name":"Aundh ","latitude":"18.558","longitude":"73.8075","city_id":"2","code":"","pincode":"411007"},
{"location_id":"312","zone_id":"10","name":"Aundh Camp ","latitude":"18.5552","longitude":"73.8189","city_id":"2","code":"","pincode":"411027"},
{"location_id":"388","zone_id":"11","name":"Aundh","latitude":"18.558","longitude":"73.8075","city_id":"2","code":"","pincode":"411007"},
{"location_id":"389","zone_id":"11","name":"Bajirao Road ","latitude":"18.5055","longitude":"73.8536","city_id":"2","code":"","pincode":"411002"},
{"location_id":"390","zone_id":"11","name":"Baner Gaon ","latitude":"18.559","longitude":"73.7868","city_id":"2","code":"","pincode":"411045"},
{"location_id":"391","zone_id":"11","name":"Baner Road ","latitude":"18.555","longitude":"73.7972","city_id":"2","code":"","pincode":"411008"},
{"location_id":"392","zone_id":"11","name":"Bavdhan ","latitude":"18.5156","longitude":"73.7819","city_id":"2","code":"","pincode":"411021"},
{"location_id":"313","zone_id":"10","name":"Bhosari I.E. ","latitude":"18.6385","longitude":"73.8478","city_id":"2","code":"","pincode":"411026"},
{"location_id":"314","zone_id":"10","name":"Bhosarigoan ","latitude":"18.5598","longitude":"73.8916","city_id":"2","code":"","pincode":"411039"},
{"location_id":"394","zone_id":"11","name":"Bhusari Colony ","latitude":"18.5082","longitude":"73.7904","city_id":"2","code":"","pincode":"411038"},
{"location_id":"315","zone_id":"10","name":"Bibvewadi ","latitude":"18.4718","longitude":"73.8671","city_id":"2","code":"","pincode":"411037"},
{"location_id":"395","zone_id":"11","name":"Botanical Garden (Pune)","latitude":"18.566","longitude":"73.8257","city_id":"2","code":"","pincode":"411020"},
{"location_id":"316","zone_id":"10","name":"C D A (O) ","latitude":"18.5204","longitude":"73.8567","city_id":"2","code":"","pincode":"411001"},
{"location_id":"317","zone_id":"10","name":"C M E ","latitude":"18.5204","longitude":"73.8567","city_id":"2","code":"","pincode":"411031"},
{"location_id":"318","zone_id":"10","name":"Chikhali ","latitude":"18.671","longitude":"73.8243","city_id":"2","code":"","pincode":"411062"},
{"location_id":"319","zone_id":"10","name":"Chinchwad East ","latitude":"18.6298","longitude":"73.7997","city_id":"2","code":"","pincode":"411019"},
{"location_id":"320","zone_id":"10","name":"Chinchwadgaon ","latitude":"18.6276","longitude":"73.7809","city_id":"2","code":"","pincode":"411033"},
{"location_id":"396","zone_id":"11","name":"Congress House Road ","latitude":"18.5228","longitude":"73.8531","city_id":"2","code":"","pincode":"411005"},
{"location_id":"322","zone_id":"10","name":"Dapodi ","latitude":"18.5129","longitude":"74.3998","city_id":"2","code":"","pincode":"411012"},
{"location_id":"321","zone_id":"10","name":"Dapodi Bazar ","latitude":"18.6233","longitude":"73.7997","city_id":"2","code":"","pincode":"411012"},
{"location_id":"397","zone_id":"11","name":"Deccan Gymkhana ","latitude":"18.5176","longitude":"73.8417","city_id":"2","code":"","pincode":"411004"},
{"location_id":"398","zone_id":"11","name":"Dhankawadi ","latitude":"18.4616","longitude":"73.8505","city_id":"2","code":"","pincode":"411043"},
{"location_id":"323","zone_id":"10","name":"Dhanori ","latitude":"18.5835","longitude":"73.8865","city_id":"2","code":"","pincode":"411015"},
{"location_id":"399","zone_id":"11","name":"Dhayari ","latitude":"18.4422","longitude":"73.8096","city_id":"2","code":"","pincode":"411041"},
{"location_id":"324","zone_id":"10","name":"Dighi Camp ","latitude":"18.5598","longitude":"73.8916","city_id":"2","code":"","pincode":"411015"},
{"location_id":"325","zone_id":"10","name":"Dr.B.A. Chowk ","latitude":"18.5214","longitude":"73.8552","city_id":"2","code":"","pincode":"411001"},
{"location_id":"327","zone_id":"10","name":"East Khadki ","latitude":"18.5699","longitude":"73.8506","city_id":"2","code":"","pincode":"411003"},
{"location_id":"400","zone_id":"11","name":"Ex. Serviceman Colony ","latitude":"18.5204","longitude":"73.8567","city_id":"2","code":"","pincode":"411038"},
{"location_id":"401","zone_id":"11","name":"Film Institute ","latitude":"18.5204","longitude":"73.8567","city_id":"2","code":"","pincode":"411004"},
{"location_id":"402","zone_id":"11","name":"Ganeshkhind ","latitude":"18.5596","longitude":"73.8171","city_id":"2","code":"","pincode":"411007"},
{"location_id":"403","zone_id":"11","name":"Ghorpade Peth ","latitude":"18.5019","longitude":"73.8663","city_id":"2","code":"","pincode":"411042"},
{"location_id":"328","zone_id":"10","name":"Ghorpuri Bazar ","latitude":"18.5282","longitude":"73.8939","city_id":"2","code":"","pincode":"411001"},
{"location_id":"404","zone_id":"11","name":"Gokhalenagar ","latitude":"18.5296","longitude":"73.8213","city_id":"2","code":"","pincode":"411016"},
{"location_id":"329","zone_id":"10","name":"Gondhale Nagar ","latitude":"18.4941","longitude":"73.9489","city_id":"2","code":"","pincode":"411028"},
{"location_id":"405","zone_id":"11","name":"Govt. Polytechnic ","latitude":"18.5204","longitude":"73.8567","city_id":"2","code":"","pincode":"411016"},
{"location_id":"406","zone_id":"11","name":"Guruwar Peth ","latitude":"18.5064","longitude":"73.8603","city_id":"2","code":"","pincode":"411042"},
{"location_id":"330","zone_id":"10","name":"H.E. Factory ","latitude":"18.5666","longitude":"73.8531","city_id":"2","code":"","pincode":"411003"},
{"location_id":"331","zone_id":"10","name":"Hadapsar ","latitude":"18.5089","longitude":"73.926","city_id":"2","code":"","pincode":"411028"},
{"location_id":"334","zone_id":"10","name":"Indrayaninagar ","latitude":"18.5495","longitude":"73.8426","city_id":"2","code":"","pincode":"411026"},
{"location_id":"335","zone_id":"10","name":"Infotech Park (Hinjawadi) ","latitude":"18.5947","longitude":"73.7095","city_id":"2","code":"","pincode":"411057"},
{"location_id":"337","zone_id":"10","name":"Kalewadi ","latitude":"18.6102","longitude":"73.7874","city_id":"2","code":"","pincode":"411017"},
{"location_id":"407","zone_id":"11","name":"Kapad Ganj ","latitude":"18.5204","longitude":"73.8567","city_id":"2","code":"","pincode":"411002"},
{"location_id":"408","zone_id":"11","name":"Karvenagar ","latitude":"18.4898","longitude":"73.8203","city_id":"2","code":"","pincode":"411052"},
{"location_id":"338","zone_id":"10","name":"Kasarwadi ","latitude":"18.6061","longitude":"73.8228","city_id":"2","code":"","pincode":"411034"},
{"location_id":"409","zone_id":"11","name":"Kasba Peth ","latitude":"18.5259","longitude":"73.861","city_id":"2","code":"","pincode":"411011"},
{"location_id":"410","zone_id":"11","name":"Katraj ","latitude":"18.4575","longitude":"73.8677","city_id":"2","code":"","pincode":"411046"},
{"location_id":"340","zone_id":"10","name":"Khadki ","latitude":"18.5699","longitude":"73.8506","city_id":"2","code":"","pincode":"411003"},
{"location_id":"339","zone_id":"10","name":"Khadki Bazar ","latitude":"18.5681","longitude":"73.8509","city_id":"2","code":"","pincode":"411003"},
{"location_id":"341","zone_id":"10","name":"Khondhwa KH ","latitude":"18.4771","longitude":"73.8907","city_id":"2","code":"","pincode":"411048"},
{"location_id":"342","zone_id":"10","name":"Kondhwa BK ","latitude":"18.4771","longitude":"73.8907","city_id":"2","code":"","pincode":"411048"},
{"location_id":"344","zone_id":"10","name":"Lohogaon ","latitude":"18.5911","longitude":"73.9188","city_id":"2","code":"","pincode":"411047"},
{"location_id":"414","zone_id":"11","name":"Lokmanyanagar ","latitude":"18.5067","longitude":"73.8457","city_id":"2","code":"","pincode":"411030"},
{"location_id":"416","zone_id":"11","name":"Mangalwar Peth (Pune)","latitude":"18.5241","longitude":"73.8647","city_id":"2","code":"","pincode":"411011"},
{"location_id":"346","zone_id":"10","name":"Market Yard (Pune)","latitude":"18.4877","longitude":"73.8684","city_id":"2","code":"","pincode":"411037"},
{"location_id":"443","zone_id":"11","name":"Swargate ","latitude":"18.5018","longitude":"73.8636","city_id":"2","code":"","pincode":"411042"},
{"location_id":"442","zone_id":"11","name":"Swargate Chowk ","latitude":"18.4987","longitude":"73.8581","city_id":"2","code":"","pincode":"411042"},
{"location_id":"440","zone_id":"11","name":"Sinhgad Technical Education Society","latitude":"18.5204","longitude":"73.8567","city_id":"2","code":"","pincode":"411041"},
{"location_id":"356","zone_id":"10","name":"Pimple Gurav ","latitude":"18.5895","longitude":"73.812","city_id":"2","code":"","pincode":"411061"},
{"location_id":"357","zone_id":"10","name":"Pimpri Colony ","latitude":"18.4929","longitude":"73.8568","city_id":"2","code":"","pincode":"411017"},
{"location_id":"426","zone_id":"11","name":"Parvati ","latitude":"18.4459","longitude":"73.8666","city_id":"2","code":"","pincode":"411009"},
{"location_id":"425","zone_id":"11","name":"Parvati Gaon ","latitude":"18.4973","longitude":"73.8511","city_id":"2","code":"","pincode":"411009"},
{"location_id":"423","zone_id":"11","name":"Narayan Peth ","latitude":"18.5155","longitude":"73.8501","city_id":"2","code":"","pincode":"411030"}]



name = ["Abhijit Jadhav",
"Abhishek  Tatti",
"Adesh Tajane",
"Aditi Jain",
"Aditya Jain",
"Aditya Dhage",
"Aditya Gaydhani",
"Adwaita Jadhav",
"Amit Dharmadhikari",
"ANAND WANI",
"Ankit Surkar",
"Ankita Purwar",
"Ashutosh Kedar",
"Atharv Vibhute",
"Chaitanya S Mamidwar",
"Darpan Bafana",
"DEEPALI ANDE",
"Dhawal bhai Patel",
"DIKSHA RAJMANE",
"Eshwar Nag Pilli",
"Gaurav Chaudhari",
"Gaurav Agarwal",
"Hussain Bohra",
"Isha Chaudhari",
"Ketan Bedarkar",
"Khemraj Adhawade",
"KIRAN SHINDE",
"Krushna Mantri",
"KUMAR NISHANT",
"Mayur Padma",
"NEEHARIKA GOYAL",
"Neha Patil",
"Nikita Dhoot",
"NISHANT GADEKAR",
"NITU CHOUDHARY",
"Piyush Chaudhari",
"Piyush Khadse",
"Pooja Chate",
"Prabhat Pandey",
"PRADNYA PATANGE",
"PRITAM KUMAR",
"Priyanka Jagtap",
"Radha Mane",
"RISHABH JHA",
"Rohit Patankar",
"Rohit Relan",
"Ronish Zadode",
"Saichand Duggirala",
"Sanket Patil",
"Sanket Raje",
"Shalaka Sawale",
"Eshank	Nazare",
"GAURAV	JAWARE",
"Indrajeet Kulkarni",
"Kanchan Patil",
"Kunal Kampassi",
"LAXMI DARANDALE",
"MANGESH RAHANE",
"MONIKA	DHAKATE",
"Niranjan Kumar",
"Nishant Shrivastava",
"Ojas Bhargave"
]

add = []

lat = []
lng = []

data = []


for i in range(len(a)):
	lat.append(a[i]["latitude"])
	lng.append(a[i]["longitude"])
	add.append(a[i]["name"])
print(len(name))
print(len(add))
print(len(lat))
print(len(lng))

'''
distance = distance_matrix(gmaps, "gokul+colony,+dighi,+pune,+IN", "college+of+engineering,+pune,+IN","driving")
print(distance['rows'][0]['elements'][0]['distance']['text'])
print(distance['rows'][0]['elements'][0]['duration']['text'])
distance = distance_matrix(gmaps, "gokul+colony,+dighi,+pune,+IN", "college+of+engineering,+pune,+IN","walking")
print(distance['rows'][0]['elements'][0]['distance']['text'])
print(distance['rows'][0]['elements'][0]['duration']['text'])
distance = distance_matrix(gmaps, "gokul+colony,+dighi,+pune,+IN", "college+of+engineering,+pune,+IN","transit")
print(distance['rows'][0]['elements'][0]['distance']['text'])
print(distance['rows'][0]['elements'][0]['duration']['text'])


import collections as co
j=1
mode_t = ['bus','2w','4w','cab']
for i in range(len(lat)):
	temp=co.OrderedDict()
	temp_mode=""
	temp.update({'id':j})
	temp.update({'name':name[i]})
	temp.update({'address':add[i]})
	temp.update({'latitude':lat[i]})
	temp.update({'longitude':lng[i]})
	temp_mode=mode_t[random.randint(0,3)]
	temp.update({'mode':temp_mode})
	if(temp_mode=='2w' or temp_mode=='4w' or temp_mode=='cab' ):
		distance2 = distance_matrix(gmaps, str(add[i])+",pune,IN", "college of engineering,pune,IN","driving")
		temp.update({'distance1':distance2['rows'][0]['elements'][0]['distance']['text']})
		temp.update({'time_req':distance2['rows'][0]['elements'][0]['duration']['text']})
	elif(temp_mode=='bus'):
		distance2 = distance_matrix(gmaps, str(add[i])+",pune,IN", "college of engineering,pune,IN","transit")
		temp.update({'distance1':distance2['rows'][0]['elements'][0]['distance']['text']})
		temp.update({'time_req':distance2['rows'][0]['elements'][0]['duration']['text']})	
	j+=1
	data.append(temp)



f=open("final_location_data.json","w")
json.dump(data,f)
'''
f=open("final_location_data.json","r")
data=json.load(f)



#print(data[0]["latitude"])
z = [[0 for x in range(2)] for y in range(len(data))]
#print(z)
for i in range(len(data)):
	z[i][0] = float(data[i]["latitude"])/100.00
	z[i][1] = float(data[i]["longitude"])/200.00
#print(z)
'''
features  = array(z)
whitened = whiten(features)
codes = 3
#book = np.array((whitened[0],whitened[2]))
print(kmeans(whitened,codes))
'''
from sklearn.cluster import KMeans
km = KMeans(n_clusters=10,max_iter=100)
print(km.fit(z))
print(km.cluster_centers_)
print(km.labels_)
cluster_labels=[]
cluster_labels=km.labels_

clusters = []
for i in range(0,10):
    temp2 = []
    for j in range(len(cluster_labels)):
        if(cluster_labels[j]==i):
            temp1 = {}
            temp1.update({'name':data[j]["name"]})
            temp1.update({'add':data[j]["address"]})
            temp2.append(temp1)
    
    clusters.append(temp2)
        

for i in clusters:
    print(i)

