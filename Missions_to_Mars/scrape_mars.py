import mission_to_mars
from bs4 import BeautifulSoup as bs
import pymongo
from splinter import Browser
import pandas as pd
import time
import pymongo
from flask import Flask, render_template, redirect

app = Flask(__name__)
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_db

@app.route('/scrape')
def scrape():
    print("Scrape route requested")
    db.mars.drop()
    db.mars.insert_one(mission_to_mars.scrape_mars())
    return redirect('/')

@app.route('/')
def index():
    print("Index route requested")
    mars_data = list(db.mars.find())
    return render_template('index.html', mars_data=mars_data)


if __name__ =="__main__":
    app.run(debug=True)