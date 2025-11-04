from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    buyer_name = db.Column(db.String(100))
    buyer_email = db.Column(db.String(120))
    address_line = db.Column(db.String(200))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    postal_code = db.Column(db.String(20))
    total_amount = db.Column(db.Float)
    shipping_fee = db.Column(db.Float)
    date_created = db.Column(db.DateTime, default=datetime.now())
    items = db.relationship("OrderItem", backref="order", lazy=True)

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"), nullable=False)