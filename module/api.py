from flask import Blueprint, render_template, jsonify, request
from . import messages


api = Blueprint('api', __name__, static_folder='static', template_folder='templates')






@api.route('/messages')
def get_messages():
    return jsonify(list(messages.find({})))


@api.route('/messages', methods=['POST'])
def create_message():
    msg = request.json['text']
    new_msg = {
        'text': msg
    }
    messages.insert_one(new_msg)
    return jsonify(new_msg)

