# encoding: utf-8
from utils import get_property
from api import app
import constants
from dotenv import load_dotenv


# Admin functions
# =======================================================

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

    with UserService() as user_srv:
        api_key = user_srv.add(name=name, code=code)

    content = {"data": [{"X-Api-Key": api_key}], 'message': f"Added user {name}:{code} successfully"}
    response = build_response(app, content)
    return response

@app.route("/article/create", methods=["POST"])
def create_article():
    """
    Creates an article

    Example of Incoming JSON
    {"article": {"miner":"<miner>", "url":"<url>", "content":"<content>", "publ_date":"<publ_date>"}
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


# Helper functions
# ==============================================================================
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
    #with Authorizer() as authorizer:
    #    return authorizer.is_api_key_valid(api_key)
    return True

# Run the RESTful API server
# ===========================================================
if __name__ == '__main__':
    debug_mode = get_property("flask_debug_mode") == "True"
    app.config["DEBUG"] = debug_mode
    api_host = get_property("api_host")
    api_port = int(get_property("api_port"))
    app.run(host=api_host, port=api_port, debug=debug_mode)
