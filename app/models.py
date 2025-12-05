from . import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "user_sign_up"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.now())
    confirmation_token = db.Column(db.String(255), unique=True)

