from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# MongoDB setup (assuming MongoDB is running locally on port 27017)
client = MongoClient("mongodb://localhost:27017")
db = client['online_store']
products_collection = db['products']
categories_collection = db['categories']

# Root route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask API!"})

# Get product catalog
@app.route('/catalog', methods=['GET'])
def get_catalog():
    products = list(products_collection.find({}, {"_id": 0}))  # Fetch all products
    return jsonify(products)

# Get categories
@app.route('/categories', methods=['GET'])
def get_categories():
    categories = list(categories_collection.find({}, {"_id": 0}))  # Fetch all categories
    return jsonify(categories)

# Add a product
@app.route('/catalog', methods=['POST'])
def add_product():
    product_data = request.json
    products_collection.insert_one(product_data)
    return jsonify({"message": "Product added successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
