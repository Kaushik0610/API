from flask import Flask,request,jsonify, make_response
import json
from pymongo import MongoClient

app=Flask(__name__)
@app.route('/register',methods=["POST"])
def register():
    data=request.get_json()
    uname=data["Username"]
    pwd=data["Password"]
    try:
        client=MongoClient("localhost",27017)
        db=client.facebook
    except:
        return jsonify({"message":"Database denied connection"})
    k=db.user.insert_one({"Username":uname,"Password":pwd})
    return jsonify({"message":"success","id":str(k)})
@app.route('/register',methods=["GET"])
def show():
    try:
        client=MongoClient("localhost",27017)
        db=client.facebook
    except:
        return jsonify({"message":"Database denied connection"})
    k=db.user.find()
    l=[]
    for i in k:
        l.append({"uname":i["Username"],"pwd":i["Password"]})
    return jsonify({"users":l})
app.run(debug=True)