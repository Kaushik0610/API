from flask import Flask,request,jsonify, make_response
import json
import uuid
from pymongo import MongoClient

app=Flask(__name__)
@app.route('/register',methods=["POST"])
def register():
    data=request.get_json()
    name=data["Name"]
    num=data["Mobile Number"]
    uid=str(uuid.uuid1())
    try:
        client=MongoClient("localhost",27017)
        db=client.train
    except:
        return jsonify({"message":"Database denied connection"})
    k=db.user.insert_one({"Name":name,"Mobile Number":num,"_id":uid})
    return jsonify({"message":"success","id":uid})
@app.route('/register',methods=["GET"])
def show():
    try:
        client=MongoClient("localhost",27017)
        db=client.train
    except:
        return jsonify({"message":"Database denied connection"})
    k=db.user.find()
    l=[]
    for i in k:
        l.append({"name":i["Name"],"num":i["Mobile Number"],"id":i["_id"]})
    return jsonify({"users":l})
app.run(debug=True)