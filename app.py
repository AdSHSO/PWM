#use to run program as web application
#python3 -m flask run

from flask import Flask, request, jsonify
from core_hashing_module import Password
from datetime import datetime

app = Flask(__name__)
user_pws = []

#curl -i -X POST -H "Content-Type: application/json" -d '{"user_id":"abcd", "clear_pw":"1234"}' http://127.0.0.1:5000/add_pw
@app.route('/add_pw', methods=['POST']) #GET requests will be blocked
def add_pw():
    # extract user id and cleartext password from incoming json
    req_data = request.get_json()
    user_id = req_data.get("user_id", "")
    clear_pw = req_data.get("clear_pw", "")

    # creat a password object
    pw = Password()
    # create a hashed password based on a cleartext password
    hashed_pw = pw.hash_password(str.encode(clear_pw))

    # create a timestamp
    dateTimeObj = datetime.now()    
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    
    # add password hash and timestamp to a dictionary
    new_entry = {"user_id": user_id,"data": {"hashed_pw": hashed_pw, "last_update": timestampStr}}
    # add dictionary to user_pws list data structure 
    user_pws.append(new_entry)

    # return successful POST -> missing what may go wrong....
    # The jsonify() function in flask returns a flask. Response() object that already has the appropriate content-type header 'application/json' for use with json responses. 
    return jsonify({"status": "ok"}), 201

#curl -i -X GET -H "Content-Type: application/json" -d '{"user_id":"abcd", "clear_pw":"1234"}' http://127.0.0.1:5000/check_pw
@app.route('/check_pw', methods=['GET']) 
def check_pw():
    
    # extract user id and cleartext password from incoming json
    req_data = request.get_json()
    user_id = req_data.get("user_id", "")
    clear_pw = req_data.get("clear_pw", "")
    
    #find entry in existing dictionary to get hash
    #for key "user_id" get hashed pw
    #get allows to specify default value if no entry
    #print((items.get("data")).get("hashed_pw"))
    #would raise key error if no entry
    #print(items["user_id"])
    for items in user_pws:
        if items.get("user_id") == user_id:
            #multiple entries per user?
            hashed_pw = (items.get("data")).get("hashed_pw")
        else:
            return jsonify("No user entry")

    #  create Password object
    pw = Password()
     
    # invoke hash_check method to compare stored hash and supplied cleartext
    if pw.hash_check(clear_pw, hashed_pw):
        return jsonify({"status": "ok"})
    else:
        return jsonify({"status": "error"})

#just for testing purpose, basic entry
@app.route('/', methods=['GET']) 
def alive():
    return jsonify("ok")


