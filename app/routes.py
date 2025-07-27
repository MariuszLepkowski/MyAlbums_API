from flask import Blueprint, jsonify, request
from app.services import show_welcome_message, get_all_albums

api = Blueprint('api', __name__)

@api.route('/', methods=['GET'])
def home_page():
    welcome_message = show_welcome_message()
    return jsonify(welcome_message), 200

@api.route('/albums', methods=['GET'])
def show_all_albums():
    albums = get_all_albums()
    return jsonify([{"id": a.id, "artist": a.artist, "title": a.title} for a in albums]), 200

