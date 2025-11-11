from flask import Flask, render_template, jsonify
import datetime
import requests
import os

app = Flask(__name__)

#Declare variables to be used by cat
catCached = None
catFetched = None

@app.route("/")
def home():
    return render_template("cat.html")

@app.route("/info")
def info():
    return render_template("catInfo.html")

@app.route("/faq")
def faq():
    return render_template("catfaq.html")

@app.route("/cat")

def cat():
    #Declare the variables inside this function as global variables
    #so they are not treated as local
    global catCached
    global catFetched

    #Get the day from the datetime library
    day = datetime.date.today()

    if not catCached or catFetched != day:
        response = requests.get("https://catfact.ninja/fact")
        fact = response.json()
        catCached = fact["fact"]
        catFetched = day
    
    return jsonify({"fact": catCached})