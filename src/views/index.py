"""
Index.py - provides a simple html example
"""
from flask import Blueprint

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


app.register_blueprint(routes)
