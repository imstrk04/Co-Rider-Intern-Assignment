from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api

app = Flask(__name__)

# Configure MongoDB
app.config['MONGO_URI'] = 'mongodb://localhost:27017/flask_mongo_app'
app.secret_key = 'thisisanassignmentforcorider'
mongo = PyMongo(app)

# Initialize Flask-RESTful API
api = Api(app)

# Import resources
from app import routes, resources

# Register resources with the API
api.add_resource(resources.UserList, '/api/users')
api.add_resource(resources.UserResource, '/api/users/<string:user_id>')

# Import routes for web views
from app import routes
