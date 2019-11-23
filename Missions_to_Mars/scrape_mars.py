from mission-to-mars import scrape_mars
from bs4 import BeautifulSoup as bs
import pymongo
from splinter import Browser
import pandas as pd
import time
import pymongo
from flask import Flask, render_template

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)


