# encoding: utf-8
"""
Flask-RESTx API registration module
======================================
"""

from flask import Flask, Blueprint
from flask_restx import Api
from .articles.resources import article as articles_ns
from .users.resources import user as users_ns
from markdown import markdown

app = Flask(__name__)
blueprint = Blueprint('api', __name__)
app.register_blueprint(blueprint)

api_desc = \
"""
This is the Zumbi API
"""

api = Api(app, title="Zumbi API", version='1.0', description=api_desc, prefix='/api/v1')
api.add_namespace(articles_ns, path='/articles')
api.add_namespace(users_ns, path='/users')

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Presents the Zumbi API README.md
    """
    with open('README.md', 'r') as f:
        return markdown(f.read())
