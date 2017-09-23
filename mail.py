import gspread
import json
import random
import geocoder
import os
import collections as co
from googlemaps.client import Client
from googlemaps.distance_matrix import distance_matrix
api_key = 'AIzaSyA47CBshq2fOEMhtM15Mu7jj9QJ5O47YxU'
gmaps = Client(api_key)
from oauth2client.service_account import ServiceAccountCredentials



def send_id(email,id_num):
    # import the smtplib module. It should be included in Python by default
    import smtplib
    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    pass1=open('/home/kde-ronz/Public/credentials.txt','r')
    pass2=pass1.read()
    MY_ADDRESS,PASSWORD=pass2.split()
    MY_ADDRESS="ronishzadode@gmail.com"
    PASSWORD="*ronish16=#"
    s.login(MY_ADDRESS, PASSWORD)
    
    # import necessary packages
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # For each contact, send the email:
    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template


    # setup the parameters of the message
    msg['From']=MY_ADDRESS
    msg['To']=email
    msg['Subject']="Smart Navigation - Allotment of ID"

    message="Hello "+email.split('@')[0]+",\n\nYour User ID is:    "+str(id_num)+"\nLogin via our Smart Navigation App to view and track your members.\nThank,you!\n\nThis mail is auto sent via python."
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s.send_message(msg)

    del msg



scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/kde-ronz/Public/deathly-null-mindspark-1ebeda70f22f.json', scope)

gc = gspread.authorize(credentials)
z=1

while True:
	print("Server is running & active since "+str(z)+" seconds\n")
	sht=gc.open('Smart Navigation (Responses)')
	v=sht.sheet1.get_all_values()
	f=open('id_cnt.txt','r')
	f1=f.read()
	f2=open('final_location_data.json','r')
	data=json.load(f2)
	f2.close()
	id_cnt,sheet_cnt=f1.split()
	id_cnt=int(id_cnt)
	sheet_cnt=int(sheet_cnt)
	mail_list = []
	for i in range(sheet_cnt+1,len(v)):
		temp = co.OrderedDict()
		id_cnt+=1
		print("New entry found:\n")
		print(v[i][2])
		send_id(v[i][1],id_cnt)
		print("Mail sent to "+v[i][2]+" with ID- "+str(id_cnt)+"\n")
		temp.update({'id':id_cnt})
		temp.update({'name':v[i][2]})
		temp.update({'address':v[i][3]})
		g=geocoder.google(str(v[i][3])+"pune,IN")
		lat=str(float(g.latlng[0]))
		lng=str(float(g.latlng[1]))
		temp.update({'latitude':lat})
		temp.update({'longitude':lng})
		
		
		if(v[i][4]=='Two wheeler'):
		    temp.update({'mode':'2w'})
		elif(v[i][4]=='Four wheeler'):
		    temp.update({'mode':'4w'})
		elif(v[i][4]=='Bus'):
		    temp.update({'mode':'bus'})
		elif(v[i][4]=='Cab'):
		    temp.update({'mode':'cab'})

		if(v[i][4]=='Two wheeler' or v[i][4]=='Four wheeler' or v[i][4]=='Cab'):
			distance2 = distance_matrix(gmaps, str(v[i][3])+",pune,IN", "college of engineering,pune,IN","driving")
			temp.update({'distance1':distance2['rows'][0]['elements'][0]['distance']['text']})
			temp.update({'time_req':distance2['rows'][0]['elements'][0]['duration']['text']})
		elif(v[i][4]=='Bus'):
			distance2 = distance_matrix(gmaps, str(v[i][3])+",pune,IN", "college of engineering,pune,IN","driving")
			temp.update({'distance1':distance2['rows'][0]['elements'][0]['distance']['text']})
			temp.update({'time_req':distance2['rows'][0]['elements'][0]['duration']['text']})

		data.append(temp)
		print("Record with ID: "+str(id_cnt)+" successfully added in json.\n")
	sheet_cnt=len(v)-1
	f.close()
	f2=open('final_location_data.json','w')
	json.dump(data,f2)
	f2.close()
	f1=open('id_cnt.txt','w')
	new_val=str(id_cnt)+" "+str(sheet_cnt)
	f1.write(new_val)
	f1.close()
	z+=1
	os.system("python groups.py")
	f2=open('start_location_data.json','r')
	data=[]
	data=json.load(f2)
	t={}
	t.update({'dB':data})
	f2.close()
	f2=open('start_location_data.json','w')
	json.dump(t,f2)
	f2.close()
	out=os.popen("git add * && git commit -m \"Add new entry\" && git push").read()
	out_t="Add new entry"
	if(out_t in out):
            print("New entries added in Database.\n\n")
