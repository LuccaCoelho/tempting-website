import uuid
from sqlalchemy.exc import IntegrityError
from flask import request, redirect, url_for, flash
from flask import get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template
from .models import User
from . import db

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    _ = get_flashed_messages()
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

@bp.route("/submit", methods=["POST"])
def submit():

    email = request.form.get("email", "").strip()
    first_name = request.form.get("first_name", "").strip()
    last_name = request.form.get("last_name", "").strip()

    if not email or not first_name or not last_name:
        flash("All fields are required.", "error")
        return redirect(url_for("main.index"))

    confirmation_token = str(uuid.uuid4())

    user = User(
        email=email,
        first_name=first_name,
        last_name=last_name,
        confirmed=False,
        confirmation_token=confirmation_token
    )

    try:
        db.session.add(user)
        db.session.commit()
        flash("Thank you!!!", "success")
    except IntegrityError:
        db.session.rollback()
        flash("Email is already signed up!", "error")
    except Exception as e:
        db.session.rollback()
        flash(f"An unexpected error occurred: {str(e)}", "error")

    return redirect(url_for("main.index") + "#user-sign-up-section")

        
