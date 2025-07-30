from flask import Blueprint, jsonify, request
from app.services import (
    show_welcome_message,
    get_all_albums,
    get_album_by_id,
    get_random_album,
    create_album,
    update_entire_album,
    update_album_partially,
    delete_album_by_id,
)
from utils.validate_album_data import (
    validate_put_data,
    validate_patch_data,
)


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

@api.route('/albums/', methods=['POST'])
def add_album():
    data = request.get_json()

    validation_error = validate_put_data(data)
    if validation_error:
        return jsonify(validation_error), 400

    album = create_album(data)

    return jsonify({
        "message": f"Successfully added {album.artist} - {album.title} to the database."
    }), 201

"""
curl -X POST http://localhost:5000/albums/ \
-H "Content-Type: application/json" \
-d '{"artist": "post_test", "title": "post_test"}'
"""

@api.route('/albums/<int:id>', methods=['PUT'])
def put_album(id):
    data = request.get_json()

    validation_error = validate_put_data(data)
    if validation_error:
        return jsonify(validation_error), 400

    album = update_entire_album(album_id=id, data=data)

    if album is None:
        return jsonify({
            "error":"The album with requested id does not exist."
        }), 404

    return jsonify({
        "message": f"Successfully updated album with id: {album.id}"
    }), 200

"""
curl -X PUT http://localhost:5000/albums/156 \
-H "Content-Type: application/json" \
-d '{"artist": "put_test", "title": "put_test"}'
"""

@api.route('/albums/<int:id>', methods=['PATCH'])
def patch_album(id):
    data = request.get_json()

    validation_error = validate_patch_data(data)
    if validation_error:
        return jsonify(validation_error), 400

    album = update_album_partially(album_id=id, data=data)

    if album is None:
        return jsonify({
            "error":"The album with requested id does not exist."
        }), 404

    return jsonify({
        "message": f"Successfully updated album with id: {album.id}"
    }), 200

"""
curl -X PATCH http://localhost:5000/albums/156 \
-H "Content-Type: application/json" \
-d '{"artist": "patch_test", "title": "patch_test"}'
"""

@api.route('/albums/<int:id>', methods=['DELETE'])
def delete_album(id):
    album = delete_album_by_id(id)

    if album is None:
        return jsonify({
            "error":"The album with requested id does not exist."
        }), 404

    return jsonify({
        "message": f"Successfully deleted album with id: {album.id} {album.artist} {album.title}"
    }), 200

"""
curl -X DELETE http://localhost:5000/albums/<album_id>
"""