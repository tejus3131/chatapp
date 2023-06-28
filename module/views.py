from flask import Blueprint, render_template, request, json, jsonify
from . import messages
from bson import json_util

views = Blueprint('views', __name__, static_folder='static', template_folder='templates')

@views.route('/')
def hello_world():
    return render_template("index.html")

@views.route('/messages')
def get_messages():
    message = []
    for msg in messages.find({}):
        message.append(json.loads(json_util.dumps(msg)))
    return message


@views.route('/messages', methods=['POST'])
def create_message():
    msg = request.form.get('msg')
    print(msg)
    new_msg = {
        'text': msg
    }
    messages.insert_one(new_msg)
    return json.loads(json_util.dumps(new_msg))

