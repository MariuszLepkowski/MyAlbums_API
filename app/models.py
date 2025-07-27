from app import db

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(128), nullable=False)
    title = db.Column(db.String(128), nullable=False)