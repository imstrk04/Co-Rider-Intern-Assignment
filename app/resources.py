from flask_restful import Resource
from flask import request, jsonify
from app import mongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash

class UserList(Resource):
    def get(self):
        users = mongo.db.users.find()
        result = [{"_id": str(user["_id"]), "name": user["name"], "email": user["email"]} for user in users]
        return jsonify(result)

    def post(self):
        data = request.get_json()
        if 'name' not in data or 'email' not in data:
            return {"error": "Name and email are required fields."}, 400
        if 'password' in data and len(data['password']) < 6:
            return {"error": "Password must be at least 6 characters long."}, 400

        new_user = {
            "name": data['name'],
            "email": data['email'],
            "password": generate_password_hash(data['password'])
        }
        mongo.db.users.insert_one(new_user)
        return {"message": "User created successfully."}, 201


class UserResource(Resource):
    def get(self, user_id):
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        if user:
            return jsonify({"_id": str(user["_id"]), "name": user["name"], "email": user["email"]})
        else:
            return {"error": "User not found."}, 404

    def put(self, user_id):
        data = request.get_json()
        if 'name' not in data or 'email' not in data:
            return {"error": "Name and email are required fields."}, 400

        updated_user = {
            "name": data['name'],
            "email": data['email'],
            "password": generate_password_hash(data['password']) if 'password' in data else None
        }
        if updated_user['password'] is None:
            del updated_user['password']

        mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": updated_user})
        return {"message": "User updated successfully."}, 200

    def delete(self, user_id):
        result = mongo.db.users.delete_one({"_id": ObjectId(user_id)})
        if result.deleted_count:
            return {"message": "User deleted successfully."}, 200
        else:
            return {"error": "User not found."}, 404
