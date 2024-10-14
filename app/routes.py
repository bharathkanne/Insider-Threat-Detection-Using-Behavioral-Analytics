from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "Insider Threat Detection System is running!"
