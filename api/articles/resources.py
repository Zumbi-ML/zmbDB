# encoding: utf-8
from db.article_service import ArticleService
from db.e_map import *
from flask import request
from flask_restx import Resource, Namespace, reqparse

parser = reqparse.RequestParser()
parser.add_argument(SOURCES, type=str, action="split")
parser.add_argument(MEDIA, type=str, action="split")
parser.add_argument(MOVEMENTS, type=str, action="split")
parser.add_argument(PEOPLE, type=str, action="split")
parser.add_argument(EDUCATIONAL, type=str, action="split")
parser.add_argument(PRIVATE, type=str, action="split")
parser.add_argument(PUBLIC, type=str, action="split")
parser.add_argument(ACTIONS, type=str, action="split")
parser.add_argument(CITIES, type=str, action="split")
parser.add_argument(STATES, type=str, action="split")
parser.add_argument(COUNTRIES, type=str, action="split")
parser.add_argument(WORKS, type=str, action="split")
parser.add_argument(POLICES, type=str, action="split")
parser.add_argument(LAWS, type=str, action="split")

article = Namespace('Article', description='Article resources')
"""
article_mdl = article.model('ArticleModel', {
    'hash': fields.Integer
})
"""

def clean_dict(dic):
    new_dic = {}
    for key in dic.keys():
        if (dic[key] != None):
            new_dic[key] = dic[key]
    return new_dic

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
        entity_criteria = clean_dict(parser.parse_args())
        with ArticleService() as article_svc:
             return article_svc.get_articles_by_criteria(entity_criteria)

    #@article.expect(article_mdl)
    def post(self):
        return True, 200


@article.route('/<hashed_uri>')
class ArticleIdResource(Resource):
    @article.response(200, "Success")
    def get(self, hashed_uri:int):
        with ArticleService() as article_svc:
            return article_svc.get_articles_by_hash(hashed_uri)
