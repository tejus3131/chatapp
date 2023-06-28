from flask import Flask, jsonify, request
import pymongo

app = Flask(__name__)
client = pymongo.MongoClient(
    "mongodb+srv://tejusgupta:tZvn1Apfs423uXnA@chatapp.5yvris0.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('chatapp')
messages = db.messages


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/messages')
def get_messages():
    return jsonify(list(messages.find()))


@app.route('/messages', methods=['POST'])
def create_message():
    msg = request.json['text']
    new_msg = {
        'text': msg
    }
    messages.insert_one(new_msg)
    return jsonify(new_msg)

if __name__ == "__main__":

    app.run(debug=True)