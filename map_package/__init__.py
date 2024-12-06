from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from map_package.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from map_package.routes import map_bp
    app.register_blueprint(map_bp, url_prefix="/")

    with app.app_context():
        db.create_all()

    return app















