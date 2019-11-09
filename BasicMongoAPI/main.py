from flask import Flask,request,jsonify, make_response
import json
from pymongo import MongoClient
app=Flask(__name__)
@app.route('/register',methods=["POST"])
def register():
    data=request.get_json()
    name=data["name"]
    mob=data["mobile"]
    try:
        client=MongoClient("localhost",27017)
        db=client.users
    except:
        return jsonify({"message":"Database denied connection"})
    k=db.user.insert_one({"name":name,"mobile":mob})
    return jsonify({"message":"success","id":str(k)})
@app.route('/register',methods=["GET"])
def show():
    try:
        client=MongoClient("localhost",27017)
        db=client.users
    except:
        return jsonify({"message":"Database denied connection"})
    k=db.user.find()
    l=[]
    for i in k:
        l.append({"name":i["name"],"mob":i["mobile"]})
    return jsonify({"users":l})
app.run(debug=True)
