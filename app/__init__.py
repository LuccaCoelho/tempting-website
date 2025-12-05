from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        try:
            db.create_all(checkfirst=True)
        except Exception as e:
            print("Database not ready yet:", e)

    migrate.init_app(app, db)
    from .routes import bp
    app.register_blueprint(bp)
    
    return app
