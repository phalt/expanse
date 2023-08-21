"""
Index.py - provides a simple html example
"""
from flask import Blueprint, request

from src.app import app
from src.rf.renderer import render_html

routes = Blueprint("index", __name__, url_prefix="/")


@routes.route("/")
@render_html()
def base_page():
    """
    This is your standard flask route and just returns a simple template file.
    RF doesn't just auto generate React frontend pages, it also does Jinja2 pages, too!
    """
    return dict(hello="world")


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


app.register_blueprint(routes)
