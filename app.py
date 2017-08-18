from flask import Flask, render_template
from flask_pymongo import PyMongo
from pymongo import MongoClient
import random

app = Flask(__name__)

# connect to MongoDB with the defaults
app.config['MONGO_DBNAME'] = 'poems'
app.config['MONGO_PORT'] = 27017

mongo = PyMongo(app)

@app.route("/")
def index():
    poems = mongo.db.cavf.find({"id" : random.randint(1,154)})
    return render_template('index.html', poems=poems)
    