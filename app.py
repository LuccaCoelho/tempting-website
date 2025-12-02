import requests
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


@app.route("/")
def index():
    albums = [
        {"title": "Album1", "image_url": "/static/images/album1.jpg"}
    ]

    products = [
        {"title": "Product1", "image_url": "/static/images/product1.png"}
    ]

    thumbnails = [
        {"title": "video1", "image_url": "/static/images/music1.jpg", "texts": ["This is the name of the album", "director: blablabla", "production: blablabla", "credits: wtv"]}
                ]
    return render_template("index.html", albums=albums, products=products, thumbnails=thumbnails)

@app.route("/api/videos")
def get_videos():
    video_ids = [
        "Qf9SOEkZR9Q&list",
        "nH7bjV0Q_44&list",
        "rK5TyISxZ_M&list"
    ]

    youtube_api_key = app.config['YOUTUBE_API_KEY']

    ids = ""

    for video in video_ids:
        ids += f", {video}"

    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={ids}$key={youtube_api_key}"
    response = requests.get(url)
    data = response.json()

    return jsonify(data)

@app.route("/Drunk-Driving")
def drunk_driving():
    return render_template("drunk_driving.html")

if __name__ == "__main__":
    app.run(app.config['DEBUG'])