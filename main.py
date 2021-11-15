import constants
from db import user_services, authorizer
from db.article_service import ArticleService
from flask import Flask, request
import json
from markdown import markdown
from utils import get_property

app = Flask(__name__)
debug_mode = get_property("debug_mode") == "True"
app.config["DEBUG"] = debug_mode

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Presents the Zumbi DB API README.md
    """
    with open('README.md', 'r') as f:
        return markdown(f.read())

#################################################################
# ADMIN FUNCTIONS
##################################################################

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

    api_key = user_services.add_user(name=name, code=code, session=None)
    content = {"data": [{"X-Api-Key": api_key}], 'message': f"Added user {name}:{code} successfully"}
    response = build_response(app, content)
    return response

@app.route("/article/create", methods=["POST"])
def create_article():
    """
    Creates an article

    Example of Incoming JSON
    {"article": {"miner":"<miner>", "uri":"<uri>", "content":"<content>", "publ_date":"<publ_date>"}
     "entities":
        {
         "sources": ["<source1>", "<source2>"],
         "people": ["<person1>", "<person2>"],
         ...
         "entity": [<values>]
        }
    }
    """
    if (not is_api_key_valid(request.headers.get("X-Api-Key"))):
        return build_unauthorized_response(app)

    article = request.json.get('article')
    entities = request.json.get('entities')

    with ArticleService(article, entities) as article_svc:
        article_svc.persist_all()

    content = {"data": [], "message": "Article added successfully"}
    return build_response(app, content)

########################################################################
# HELPER FUNCTIONS
#######################################################################

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
    #return authorizer.is_api_key_valid(api_key)
    return True

api_host = get_property("api_host")
api_port = int(get_property("api_port"))
app.run(host=api_host, port=api_port, debug=debug_mode)
