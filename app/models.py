from app import mongo
from werkzeug.security import generate_password_hash

def get_all_users():
    return mongo.db.users.find()

def add_user(data):
    data['password'] = generate_password_hash(data['password'])
    return mongo.db.users.insert_one(data)

def get_user(user_id):
    return mongo.db.users.find_one({"_id": user_id})

def update_user(user_id, data):
    if 'password' in data:
        data['password'] = generate_password_hash(data['password'])
    return mongo.db.users.update_one({"_id": user_id}, {"$set": data})

def delete_user(user_id):
    return mongo.db.users.delete_one({"_id": user_id})
