import csv
import os
from app import create_app, db
from app.models import Album  # model name from app/models.py

CSV_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'albums.csv')

def load_albums_from_csv():
    app = create_app()
    with app.app_context():
        with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                album = Album(artist=row['artist'], title=row['album'])
                db.session.add(album)
            db.session.commit()
            print("Data loaded to database.")

if __name__ == "__main__":
    load_albums_from_csv()
