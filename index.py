from flask import Flask, request, jsonify, redirect
from pymongo import MongoClient
from bson import ObjectId
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Replace with your MongoDB connection URI
client = MongoClient(
    'mongodb+srv://tejusgupta:tZvn1Apfs423uXnA@chatapp.5yvris0.mongodb.net/?retryWrites=true&w=majority')
db = client['chatdb']  # MongoDB database instance

# Route to retrieve all messages

@app.route('/')
def index():
    return 'This is an API server. It is not intended for GUI use. <a href="/clear">Clear Messaages</a>'


@app.route('/messages', methods=['GET'])
def get_messages():
    messages = list(db.messages.find())
    # Convert ObjectId to string for JSON serialization
    messages = [{**message, '_id': str(message['_id'])}
                for message in messages]
    return jsonify(messages)

# Route to create a new message


@app.route('/messages', methods=['POST'])
def create_message():
    content = request.json['content']

    message = {'content': content}
    db.messages.insert_one(message)

    # Convert ObjectId to string for JSON serialization
    message['_id'] = str(message['_id'])
    return jsonify(message)

# Route to delete a message
@app.route('/clear')
def clear_messages():
    db.messages.delete_many({})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
