"""
Index.py - provides a simple html example
"""
from datetime import datetime
from random import randint
from time import sleep

from flask import Blueprint, request

from src.app import app
from src.rf.renderer import render_html

routes = Blueprint("htmx", __name__, url_prefix="/")


@routes.route("/htmx")
@render_html()
def htmx():
    return dict()


@routes.route("/other-page")
def other_page():
    return "<p>This is the content of the other page!</p>"


@routes.route("/post-example", methods=["POST"])
def post():
    return f"<li>{request.form['item']}</li>"


@routes.route("/poll", methods=["GET"])
@render_html()
def poll():
    return dict(time=datetime.now().strftime("%H:%M:%S"))


@routes.route("/loading", methods=["GET"])
@render_html()
def loading():
    sleep(4)
    return dict()


@routes.route("/progress", methods=["POST"])
@render_html()
def progress():
    total_time = int(request.form.get("total_time", 0))
    if total_time > 100:
        return dict(finished=True)
    else:
        delay = randint(1, 10)
        return dict(finished=False, total_time=total_time + delay, delay=delay)


app.register_blueprint(routes)
