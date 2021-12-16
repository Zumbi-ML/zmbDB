# encoding: utf-8
import article_manager
from db.article_service import ArticleService
from flask_restx import Resource, Namespace, reqparse
import json
from labels import *
from zmbapi_exceptions import ZmbDuplicateEntryException
from utils import build_response_json
from constants import HTTP_OK, HTTP_CREATED, HTTP_INTERNAL_SERVER_ERROR

parser = reqparse.RequestParser()
parser.add_argument(AUTHORS, type=str)
parser.add_argument(CONTENT, type=str)
parser.add_argument(ENTITIES, type=str)
parser.add_argument(KEYWORDS, type=str)
parser.add_argument(MINER, type=str)
parser.add_argument(PUBLISHED_TIME, type=str)
parser.add_argument(SECTION, type=str)
parser.add_argument(SITE_NAME, type=str)
parser.add_argument(SOURCE, type=str)
parser.add_argument(TITLE, type=str)
parser.add_argument(URL, type=str)

article = Namespace('Article', description='Article resources')

@article.route('/')
class ArticleResource(Resource):

    @article.expect(parser)
    @article.response(200, "Success")
    def get(self):
        """
        Retrieves the articles that matches the passed entities

        Example of incoming JSON data
        {"sources":["src1"], "media":["med1","med2","med3"]}}
        """
        entity_criteria = parser.parse_args()
        with ArticleService() as article_svc:
             return article_svc.get_articles_by_criteria(entity_criteria)

    @article.expect(parser)
    def post(self):
        """
        Adds an article to the database.
        Expected format:
        {
            "authors": "author1,author2",
            "content": "article content",
            "entities": {"<entity_label>": ["<entity1>", "<entity2>"]},
            "keywords": "keyword1,keyword2,..."
            "miner": "zmb-scrapper",
            "published_time": "YYYY-mm-dd",
            "section": "The section of the paper",
            "site_name": "The name of the site",
            "source": "The name of the source",
            "title": "the article's title",
            "url": "http://domain.com/article.shtml"
        }
        """
        parsed_args = parser.parse_args()
        article_map = article_manager.parsed_args_2_article_map(parsed_args)
        hashed_url = hash(article_map['url'])
        try:
            article_manager.add_article(article_map)
        except ZmbDuplicateEntryException as e:
            return build_response_json(hashed_url, str(e), HTTP_INTERNAL_SERVER_ERROR)
        return build_response_json(hashed_url, "success", HTTP_CREATED)

@article.route('/<hashed_url>')
class ArticleIdResource(Resource):

    @article.response(200, "Success")
    def get(self, hashed_url:int):
        """
        Gets an article's entities by hash
        """

        with ArticleService() as article_svc:
            return article_svc.get_articles_by_hash(hashed_url)
