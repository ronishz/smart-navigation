'''import urllib2
import json


hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
response = urllib2.urlopen('https://path-d2f47.firebaseio.com')
#data = json.load(response)   
print resp
'''
import json
from firebase import firebase
firebase = firebase.FirebaseApplication('https://path-d2f47.firebaseio.com', None)
result = firebase.get('/dB',None)

data={'latitude':'18.558','name':'Xavier','longitude':'73.8075','address':'Aundh'}
s=json.dumps(data)
#result=firebase.post('/dB',s)
#result = firebase.post('/users', str(""), {'print': 'pretty'}, {'X_FANCY_HEADER': 'VERY FANCY'})
print(result)