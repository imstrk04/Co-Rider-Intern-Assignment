from flask import Flask
from flask_pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__)

# Configure MongoDB
app.config['MONGO_URI'] = 'mongodb://localhost:27017/flask_mongo_app'
app.secret_key = 'thisisanassignmentforcorider'
mongo = PyMongo(app)

# Import routes
from app import routes
