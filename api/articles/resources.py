# encoding: utf-8
import article_manager
from db.article_service import ArticleService
from flask_restx import Resource, Namespace, reqparse
import json
from labels import *
from zmbapi_exceptions import ZmbDuplicateKeyException
from zmb_codes import StatusCode
from zmb_labels import ZmbLabels
from responder import json_response
from hasher import hash_url

parser = reqparse.RequestParser()
for label in ZmbLabels.Article.all_labels():
    parser.add_argument(label, type=str)

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
        Expected format: (Check ZmbLabels.Article labels)
        {
            "authors": "author1,author2",
            "content": "article content",
            "entities": {"<entity_label>": ["<entity1>", "<entity2>"]},
            "keywords": "keyword1,keyword2,..."
            "miner": "zmbnews-scrapper",
            "published_time": "YYYY-mm-dd",
            "section": "The section of the paper",
            "site_name": "The name of the site",
            "sources": "The name of the source",
            "title": "the article's title",
            "url": "http://a-domain.com/article.shtml",
            "html": "<html><body></body></html>",
            "meta_data": "article's metadata",
        }
        """
        parsed_args = parser.parse_args()

        article_map = article_manager.setup_types(parsed_args)
        hashed_url = article_map['hashed_url']
        try:
            article_manager.add_article_n_entities(article_map)
        except ZmbDuplicateKeyException as e:
            msg = f"{hashed_url}\t{str(e)}"
            status_code = StatusCode.DUPLICATE_KEY.code()
            return json_response(status_code=status_code, message=msg)
        return json_response(status_code=StatusCode.SUCCESS.code(), message=article_map['url'])

@article.route('/<hashed_url>')
class ArticleIdResource(Resource):

    @article.response(200, "Success")
    def get(self, hashed_url:str):
        """
        Gets an article's entities by hash
        """
        return article_manager.get_by_hash(hashed_url)
