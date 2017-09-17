import json
f=open("start_location_data.json","r")
f1=json.load(f)
new=str("{\"dB\":")+f1+str("}")
f=open("start_location_data.json","w")
json.dump(new,f)
