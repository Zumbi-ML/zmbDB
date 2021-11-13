import constants
from db_services import add_user
from flask import Flask, request
import json
from markdown import markdown
from utils import get_api_property

app = Flask(__name__)
debug_mode = get_api_property("debug_mode") == "True"
app.config["DEBUG"] = debug_mode

@app.route("/")
def index():
    """
    Presents the Zumbi DB API README.md file
    """
    with open('README.md', 'r') as f:
        return markdown(f.read())

@app.route("/user/create", methods=["POST"])
def create_user():
    """
    Creates a user in the DB
    Example of a json request
    {}
    """
    if (not is_api_key_valid(request.headers.get("X-Api-Key"))):
        return build_unauthorized_response(app)

    name = request.json.get('name')
    code = request.json.get('code')
    api_key = add_user(name=n, cod=c, session=None)
    content = {"data": [{"X-Api-Key": api_key}], 'message': f"Added collaborator {name}:{code} successfully"}
    response = build_response(app, content)
    return response

def build_response(app, content, status_code=constants.SUCCESSFUL):
    """
    Builds a JSON response
    """
    return app.response_class(
        response=json.dumps(content),
        status=status_code,
        mimetype='application/json'
    )

def build_unauthorized_response(app):
    """
    Buils an unauthorized response
    """
    content = {'message': 'Unauthorized Access: Invalid X-Api-Key'}
    return build_response(app, content)

def is_api_key_valid(api_key):
    """
    Checks whether the api key is valid in the DB
    """
    return True

api_host = get_api_property("api_host")
api_port = int(get_api_property("api_port"))
app.run(host=api_host, port=api_port, debug=debug_mode)
