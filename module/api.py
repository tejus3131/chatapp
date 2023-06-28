from flask import Blueprint, render_template, jsonify, request, json
from . import messages
from bson import json_util


api = Blueprint('api', __name__, static_folder='static', template_folder='templates')

@api.route('/messages')
def get_messages():
    message = []
    for msg in messages.find({}):
        message.append(json.loads(json_util.dumps(msg)))
    return jsonify(message)


@api.route('/messages', methods=['POST'])
def create_message():
    msg = request.json['msg']
    print(msg)
    new_msg = {
        'text': msg
    }
    messages.insert_one(new_msg)
    return jsonify(json.loads(json_util.dumps(new_msg)))


@api.route("/clear", methods=["GET"])
def clear():
    messages.delete_many({})
    return jsonify({"success": True})