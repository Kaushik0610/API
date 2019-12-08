from flask import Flask,request,jsonify, make_response
import json
app=Flask(__name__)
@app.route('/show',methods=["GET"])
def meme():
    data= request.get_json()
    meme=data["meme"]
    meme=meme+" hosts meme review."
    return jsonify({"message":meme})
@app.route('/show/<meme>',methods=["GET"])
def meme1(meme):
    meme=meme+" hosts meme review."
    return jsonify({"message":meme})
app.run(debug=True)