from flask import Flask,request,jsonify, make_response
import json
app=Flask(__name__)
@app.route('/show',methods=["GET"])
def hello():
    data= request.get_json()
    name=data["name"]
    name="Hello,"+name
    return jsonify({"message":name})
@app.route('/show/<name>',methods=["GET"])
def hello1(name):
    name="Hello,"+name
    return jsonify({"message":name})
app.run(debug=True)