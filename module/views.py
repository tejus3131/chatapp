from flask import Blueprint, render_template

views = Blueprint('views', __name__, static_folder='static', template_folder='templates')

@views.route('/')
def hello_world():
    return render_template("index.html")