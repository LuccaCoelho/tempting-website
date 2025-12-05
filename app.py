import requests
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


@app.route("/")
def index():
    albums = [
        {"title": "Truth or Dare", 
         "image_url": "/static/images/cover/WhatsApp Image 2025-12-04 at 13.24.38.jpeg",
         "writers": "Faith Winkler, Zane Smith",
         "producers": "Zane Smith",
         "linktree": "https://distrokid.com/hyperfollow/tempting/truth-or-dare"}
    ]
    
    thumbnails = [
        {"title": "Truth or Dare", 
         "thumbnail": "/static/images/thumbanils/WhatsApp Image 2025-12-03 at 16.07.50.jpeg", 
         "ID": "BMMSUV3AyhE",
         "director": "Alex Killian",
         "producer": "Zane Smith",
         "leading_roles": "Faith Winkler, Lucca Coelho"}
        ]
    return render_template("index.html", albums=albums, thumbnails=thumbnails)

if __name__ == "__main__":
    app.run()