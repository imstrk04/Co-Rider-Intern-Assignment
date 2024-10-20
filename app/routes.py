from flask import request, render_template, redirect, url_for, flash
from app import app, mongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash 

def validate_user_data(data):
    if 'name' not in data or 'email' not in data:
        return False, {"error": "Name and email are required fields."}
    if 'password' in data and len(data['password']) < 6:
        return False, {"error": "Password must be at least 6 characters long."}
    return True, None

@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    result = [{"_id": str(user["_id"]), "name": user["name"], "email": user["email"]} for user in users]
    return render_template('user_list.html', users=result)

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = mongo.db.users.find_one({"_id": ObjectId(id)})
    if user:
        return render_template('user_detail.html', user={"_id": str(user["_id"]), "name": user["name"], "email": user["email"]})
    else:
        flash("User not found", "danger")
        return redirect(url_for('get_users'))

@app.route('/users/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        data = request.form
        is_valid, error_response = validate_user_data(data)
        if not is_valid:
            flash(error_response['error'], 'danger')
            return redirect(url_for('create_user'))

        new_user = {
            "name": data['name'],
            "email": data['email'],
            "password": generate_password_hash(data['password']) 
        }
        mongo.db.users.insert_one(new_user)
        flash("User created successfully", 'success')
        return redirect(url_for('get_users'))

    return render_template('add_user.html')

@app.route('/users/<id>/edit', methods=['GET', 'POST'])
def update_user(id):
    user = mongo.db.users.find_one({"_id": ObjectId(id)})
    if request.method == 'POST':
        data = request.form
        is_valid, error_response = validate_user_data(data)
        if not is_valid:
            flash(error_response['error'], 'danger')
            return redirect(url_for('update_user', id=id))

        updated_user = {
            "name": data['name'],
            "email": data['email'],
            "password": generate_password_hash(data['password']) if 'password' in data else None
        }
        if updated_user['password'] is None:
            del updated_user['password']

        mongo.db.users.update_one({"_id": ObjectId(id)}, {"$set": updated_user})
        flash("User updated successfully", 'success')
        return redirect(url_for('get_users'))
    
    return render_template('update_user.html', user={"_id": str(user["_id"]), "name": user["name"], "email": user["email"]})

@app.route('/users/<id>/delete', methods=['POST'])
def delete_user(id):
    result = mongo.db.users.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        flash("User deleted successfully", 'success')
    else:
        flash("User not found", 'danger')
    return redirect(url_for('get_users'))
