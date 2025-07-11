from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.routes import api
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(api)

    with app.app_context():
        from app import models

    return app
