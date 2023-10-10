from pymongo import MongoClinet
from pymongo.collection import Collection
from bson import ObjectId
from datetime import datetime
import os

class Professor:
    def __init__(self,first_name,last_name, email, school_name, city,state):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.school_name = school_name
        self.city = city
        self.state = state
        