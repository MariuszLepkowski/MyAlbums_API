from app.models import Album
from app.extensions import db

def show_welcome_message():
    return {"message": "Welcome to MyAlbums_API!"}

def get_all_albums():
    all_albums = db.session.execute(db.select(Album).order_by(Album.id)).scalars().all()
    return all_albums
    # alternatively  return Album.query.order_by(Album.id).all()
