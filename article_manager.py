# -*- coding: UTF-8 -*-

from datetime import date
from db.article_service import ArticleService
import json
from sqlalchemy.exc import IntegrityError
from zmbapi_exceptions import ZmbDuplicateEntryException

def parsed_args_2_article_map(parsed_args):
    """
    Converts a parsed_args object into an article_map that can be used to insert
    into the database
    """
    # Hash the url
    parsed_args['hashed_url'] = hash(parsed_args['url'])

    # The entities come as a JSON string. We convert it to a dictionary
    parsed_args['entities'] = json.loads(parsed_args['entities'])

    # Converts publish_time to a date object
    published_time = None
    if (not parsed_args['published_time']):
        published_time = parsed_args['published_time']
        year, month, day = published_time.split("-")
        published_time = date(year, month, day)
    parsed_args['published_time'] = published_time

    return parsed_args

def add_article(article_map):
    """
    Adds an article to the database
    """
    try:
        with ArticleService() as article_svc:
            article_svc.persist_article_n_entities(article_map)
    except IntegrityError as e:
        url = article_map['url']
        raise ZmbDuplicateEntryException(f"Article already in the database\n{url}")
