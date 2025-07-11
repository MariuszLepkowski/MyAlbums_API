from flask import Blueprint, jsonify, request
from app.services import greet_user

api = Blueprint('api', __name__)

@api.route('/', methods=['GET'])
def home_page():
    welcome_message = greet_user()
    return jsonify(welcome_message), 200
