from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

messages = []

@app.route('/')
def index():
    return 'This is an API server. It is not intended for GUI use.'

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

@app.route('/messages', methods=['POST'])
def add_message():
    content = request.json.get('content')
    sender = request.json.get('sender')

    if content and sender:
        message = {
            'content': content,
            'sender': sender
        }
        messages.append(message)
        return jsonify({'message': 'Message sent successfully'})
    else:
        return jsonify({'error': 'Missing content or sender'}), 400
    
@app.route("/clear")
def clear_messages():
    messages.clear()
    return jsonify({'message': 'Messages cleared successfully'})

if __name__ == '__main__':
    app.run(debug=True)
