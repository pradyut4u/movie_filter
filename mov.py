from flask import Flask,jsonify,request
import csv

movlist = []

with open("mov.csv")as f:
    csvreader = csv.reader(f)
    data = list(csvreader)
    movlist = data[1:]

likemov = []
dislikemov = []
notseen = []

app = Flask(__name__)

@app.route("/getmovie")

def getmovie():
    return jsonify({
        "data":movlist[0],
        "status":"success"
    })

@app.route("/likemovie",methods = ["POST"])

def likemovie():
    movie = movlist[0]
    movlist = movlist[1:]
    likemov.append(movie)
    return jsonify({
        "status":"success"
    }),201

@app.route("/dislikemovie",methods = ["POST"])

def dislikemovie():
    movie1 = movlist[0]
    movlist = movlist[1:]
    dislikemov.append(movie1)
    return jsonify({
        "status":"success"
    }),201

@app.route("/notwatched",methods = ["POST"])

def notwatched():
    movie2 = movlist[0]
    movlist = movlist[1:]
    notseen.append(movie2)
    return jsonify({
        "status":"success"
    }),201

if __name__ == "__main__":
    app.run()