from flask import Flask,jsonify,request
import csv

artlist = []

with open("art.csv")as f:
    csvreader = csv.reader(f)
    data = list(csvreader)
    artlist = data[1:]

likeart = []
dislikeart = []
notread = []

app = Flask(__name__)

@app.route("/getarticle")

def getarticle():
    return jsonify({
        "data":artlist[0],
        "status":"success"
    })

@app.route("/likearticle",methods = ["POST"])

def likearticle():
    article = artlist[0]
    artlist = artlist[1:]
    likeart.append(article)
    return jsonify({
        "status":"success"
    }),201

@app.route("/dislikearticle",methods = ["POST"])

def dislikearticle():
    article1 = artlist[0]
    artlist = artlist[1:]
    dislikeart.append(article1)
    return jsonify({
        "status":"success"
    }),201

@app.route("/notwatched",methods = ["POST"])

def notwatched():
    article2 = artlist[0]
    artlist = artlist[1:]
    notseen.append(article2)
    return jsonify({
        "status":"success"
    }),201

if __name__ == "__main__":
    app.run()