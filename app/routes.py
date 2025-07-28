from flask import Blueprint, jsonify, request
from app.services import show_welcome_message,get_all_albums, get_album_by_id, get_random_album


api = Blueprint('api', __name__)

@api.route('/', methods=['GET'])
def home_page():
    welcome_message = show_welcome_message()
    return jsonify(welcome_message), 200

@api.route('/albums/', methods=['GET'])
def show_all_albums():
    albums = get_all_albums()
    return jsonify([{"id": a.id, "artist": a.artist, "title": a.title} for a in albums]), 200

@api.route('/albums/<int:album_id>', methods=['GET'])
def pick_album_by_id(album_id):
    picked_album = get_album_by_id(id=album_id)

    if picked_album is None:
        return jsonify({
            "error":"The album with requested id does not exist."
        }), 404

    return jsonify({
        "id": picked_album.id,
        "artist": picked_album.artist,
        "title": picked_album.title},
    ), 200

@api.route('/albums/random', methods=['GET'])
def pick_random_album():
    random_album = get_random_album()
    return jsonify({
        "id": random_album.id,
        "artist": random_album.artist,
        "title": random_album.title},
    ), 200
