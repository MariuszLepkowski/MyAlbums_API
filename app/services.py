from app.models import Album
from app.extensions import db
from sqlalchemy.exc import NoResultFound
import random

def show_welcome_message():
    return {"message": "Welcome to MyAlbums_API!"}

def get_all_albums():
    all_albums = db.session.execute(db.select(Album).order_by(Album.id)).scalars().all()
    return all_albums
    # alternatively  return Album.query.order_by(Album.id).all()

def get_album_by_id(id):
    try:
        album = db.session.execute(db.select(Album).filter_by(id=id)).scalar_one()
        return album
    except NoResultFound:
        return None

def get_random_album():
    albums = get_all_albums()
    random_album = random.choice(albums)
    return random_album

def create_album(data):
    new_album = Album(artist=data["artist"], title=data["title"])

    db.session.add(new_album)
    db.session.commit()

    return new_album

def update_entire_album(album_id, data):
    album = get_album_by_id(album_id)
    if album is None:
        return None

    album.artist = data["artist"]
    album.title = data["title"]

    db.session.commit()

    return album

def update_album_partially(album_id, data):
    album = get_album_by_id(album_id)
    if album is None:
        return None

    if 'artist' in data and data["artist"]:
        album.artist = data["artist"]
    if 'title' in data and data["title"]:
        album.title = data["title"]

    db.session.commit()

    return album

def delete_album_by_id(album_id):
    album = get_album_by_id(album_id)

    if album is None:
        return None

    db.session.delete(album)
    db.session.commit()
    return album







