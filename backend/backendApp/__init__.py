from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
app.config["SECRET_KEY"] = "9373e2050b7e48109500d1885696c3c985243c50"

# todo fill in mongo uri with your own username and password
app.config["MONGO_URI"] = "mongodb+srv://<username>:<password>@cluster0.1poypni.mongodb.net/?retryWrites=true&w=majority"

# set up mongo db
# mongodb_client = PyMongo(app)
# db = mongodb_client.db
# print("Connected to MongoDB!",  db)

client = MongoClient(app.config["MONGO_URI"])
db = client.db

from backendApp import exampleScript
from backendApp import routes
