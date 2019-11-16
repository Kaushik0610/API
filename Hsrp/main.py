from flask import Flask,request,jsonify, make_response
import json
from pymongo import MongoClient
app=Flask(__name__)
@app.route('/register',methods=["POST"])
def register():
    data=request.get_json()
    name=data["name"]
    age=data["age"]
    sex=data["sex"]
    dis=data["disease"]
    try:
        client=MongoClient("localhost",27017)
        db=client.Hospital
    except:
        return jsonify({"message":"Database denied connection"})
    k=db.patient.insert_one({"name":name,"age":age,"sex":sex,"disease":dis})
    try:
        k1=db.disease.find_one({"name":dis})
        count=int(k1["count"])+1
        print(count)
        db.disease.update_one({"name":dis},{"$set":{"count":count}})
    except:
        k1=db.disease.insert({"name":dis,"count":1})
    return jsonify({"message":"success","id":str(k)})
@app.route('/register',methods=["GET"])
def show():
    try:
        client=MongoClient("localhost",27017)
        db=client.Hospital
    except:
        return jsonify({"message":"Database denied connection"})
    k=db.patient.find()
    l=[]
    for i in k:
        l.append({"name":i["name"],"age":i["age"],"sex":i["sex"],"dis":i["disease"]})
    return jsonify({"Hospital":l})
@app.route('/disease',methods=["GET"])
def disease1():
    try:
        client=MongoClient("localhost",27017)
        db=client.Hospital
    except:
        return jsonify({"message":"Database denied connection"})
    k=db.disease.find()
    l=[]
    for i in k:
        l.append({"disease":i["name"],"count":i["count"]})
    return jsonify({"Hospital":l})
app.run(debug=True)
