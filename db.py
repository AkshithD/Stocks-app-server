from flask import Blueprint, jsonify, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

bp = Blueprint('api', __name__)

# Connect to MongoDB
uri = os.environ.get('dburl')

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['stocks-app']
users_collection = db['users']

# Ping the MongoDB deployment to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Example route to fetch users
@bp.route('/users', methods=['GET'])
def get_users():
    users = list(users_collection.find({}, {'_id': 0}))  # Exclude the '_id' field from the response
    return jsonify(users)

@bp.route('/users/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        # Handle the OPTIONS request
        response_headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
        return '', 200, response_headers

    if request.method == 'POST':
        user_data = request.json

        # Find the user in the database based on email and password
        user = users_collection.find_one({'email': user_data['email'], 'password': user_data['password']})

        if user:
            # User found, perform login actions (e.g., generate a session or token)
            # Return a success message or token to the client
            return jsonify(message='Login successful'), 200
        else:
            # User not found or incorrect credentials, return an error message
            return jsonify(error='Invalid email or password'), 401


# Example route to create a new user
@bp.route('/users/signup', methods=['POST', 'OPTIONS'])
def create_user():
    if request.method == 'OPTIONS':
        # Handle the OPTIONS request
        response_headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
        return '', 200, response_headers

    if request.method == 'POST':
        user_data = request.json

        # Check if the user already exists
        existing_user = users_collection.find_one({'email': user_data['email']})
        if existing_user:
            return jsonify(error='User already exists'), 400
        result = users_collection.insert_one(user_data)

        if result.inserted_id:
            return jsonify(message='User created successfully'), 201
        else:
            return jsonify(error='User creation failed'), 500

from bson import json_util

@bp.route('/users/<email>', methods=['GET'])
def get_user(email):
    user = users_collection.find_one({'email': email})

    # Serialize the user using json_util
    serialized_user = json_util.dumps(user)

    # Return the serialized user
    return serialized_user, 200, {'Content-Type': 'application/json'}

@bp.route('/users/<email>/portfolio', methods=['GET'])
def get_user_stocks(email):
    user = users_collection.find_one({'email': email})

    # Serialize the user using json_util
    serialized_user = json_util.dumps(user['portfolio'])

    # Return the serialized user
    return serialized_user, 200, {'Content-Type': 'application/json'}

@bp.route('/users/<email>/portfolio', methods=['POST', 'OPTIONS'])
def add_user_stock(email):
    if request.method == 'OPTIONS':
        # Handle the OPTIONS request
        response_headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
        return '', 200, response_headers

    if request.method == 'POST':
        user_data = request.json
        print(user_data)
        users_collection.update_one({'email': email}, {'$push': {'portfolio': user_data}})
        return jsonify(message='Stock added successfully')
    
@bp.route('/users/<email>/portfolio/<symbol>', methods=['DELETE'])
def delete_user_stock(email,symbol):
    users_collection.update_one({'email': email}, {'$pull': {'portfolio': {'symbol': symbol}}})
    return jsonify(message='Stock deleted successfully')

@bp.route('/users/<email>/watchlist', methods=['GET'])
def get_user_watchlist(email):
    user = users_collection.find_one({'email': email})

    # Serialize the user using json_util
    serialized_user = json_util.dumps(user['watchlist'])

    # Return the serialized user
    return serialized_user, 200, {'Content-Type': 'application/json'}

@bp.route('/users/<email>/watchlist', methods=['POST', 'OPTIONS'])
def add_user_watchlist(email):
    if request.method == 'OPTIONS':
        # Handle the OPTIONS request
        response_headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
        return '', 200, response_headers

    if request.method == 'POST':
        user_data = request.json
        print(user_data)
        users_collection.update_one({'email': email}, {'$push': {'watchlist': user_data}})
        return jsonify(message='Stock added successfully')
    
@bp.route('/users/<email>/watchlist/<symbol>', methods=['DELETE'])
def delete_user_watchlist(email,symbol):
    users_collection.update_one({'email': email}, {'$pull': {'watchlist': {'symbol': symbol}}})
    return jsonify(message='Stock deleted successfully')

# Example route to update a user
@bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.json
    users_collection.update_one({'_id': user_id}, {'$set': user_data})
    return jsonify(message='User updated successfully')

# Example route to delete a user
@bp.route('/users/<email>', methods=['DELETE'])
def delete_user(email):
    users_collection.delete_one({'email': email})
    print("Deleted user:", email, "successfully")
    return jsonify(message='User deleted successfully')
