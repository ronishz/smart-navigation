f=open("start_location_data.json","r")
data=json.load(f)
data=data["dB"]

for i in range(len(data)):
	data[i]["group_id"]