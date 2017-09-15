from flask import Flask
import json
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():    
    f=open("final_location_data.json","r")
    data=json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 
