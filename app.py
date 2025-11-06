from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route("/")
def index():
    albums = [
        {"title": "Album1", "image_url": "/static/images/album1.jpg"},
        {"title": "Album2", "image_url": "/static/images/album2.jpg"},
        {"title": "Album3", "image_url": "/static/images/album3.jpg"},
    ]

    products = [
        {"title": "Product1", "image_url": "/static/images/product1.png"},
        {"title": "Product2", "image_url": "/static/images/product2.jpg"},
        {"title": "Product3", "image_url": "/static/images/product3.jpeg"},
        {"title": "Product4", "image_url": "/static/images/product4.jpg"}
    ]
    return render_template("index.html", albums=albums, products=products)

if __name__ == "__main__":
    app.run(debug=True)