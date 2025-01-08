from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# MongoDB connection setup
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]
collection = db.get_collection("tasks") 
# Routes

# Get all passwords
@app.route('/', methods=['GET'])
def get_passwords():
    tasks = list(collection.find({}))
    # Convert _id to string for JSON serialization
    for password in tasks:
        password["_id"] = str(password["_id"])
    return jsonify(tasks)

# Save a password
@app.route('/', methods=['POST'])
def save_password():
    password = request.json
    result = collection.insert_one(password)
    return jsonify({"success": True, "result": str(result.inserted_id)})

# Delete a password by id
@app.route('/', methods=['DELETE'])
def delete_password():
    password = request.json
    result = collection.delete_one(password)
    return jsonify({"success": True, "result": result.deleted_count})

# Start the server
if __name__ == '__main__':
    app.run(port=3000)
