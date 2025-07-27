from flask import Blueprint, jsonify, request
from app.services import show_welcome_message

api = Blueprint('api', __name__)

@api.route('/', methods=['GET'])
def home_page():
    welcome_message = show_welcome_message()
    return jsonify(welcome_message), 200
