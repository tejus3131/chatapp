from flask import Flask, jsonify, request, render_template, Blueprint
import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://tejusgupta:tZvn1Apfs423uXnA@chatapp.5yvris0.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('chatapp')
messages = db.messages


def create_app():

    app = Flask(__name__)
    from .api import api
    from .views import views
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(views, url_prefix='/')

    return app

