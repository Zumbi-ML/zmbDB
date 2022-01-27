# -*- coding: UTF-8 -*-

from datetime import date
from db.article_service import ArticleService
import json
from sqlalchemy.exc import IntegrityError
from zmbapi_exceptions import ZmbDuplicateKeyException
from hasher import hash_url
from zmb_labels import ZmbLabels

def setup_types(parsed_args):
    """
    Converts a parsed_args object into an article_map that can be used to insert
    into the database
    """
    # Hash the url
    hashed_url_lbl = ZmbLabels.Article.HashedURL.api()
    url_lbl = ZmbLabels.Article.URL.api()
    parsed_args[hashed_url_lbl] = hash_url(parsed_args[url_lbl])

    # The entities come as a JSON string. We convert it to a dictionary
    entities_lbl = ZmbLabels.Article.Entity.api()
    parsed_args[entities_lbl] = json.loads(parsed_args[entities_lbl])

    # Converts publish_time to a date object
    published_time_lbl = ZmbLabels.Article.PublishedTime.api()
    published_time = None
    if (parsed_args[published_time_lbl]):
        published_time = parsed_args[published_time_lbl]
        year, month, day = published_time.split("-")
        year, month, day = int(year), int(month), int(day)
        published_time = date(year, month, day)
    parsed_args[published_time_lbl] = published_time

    return parsed_args

def add_article_n_entities(article_map):
    """
    Adds an article to the database
    """
    try:
        with ArticleService() as article_svc:
            article_svc.persist_article_n_entities(article_map)
    except IntegrityError as e:
        url = article_map['url']
        raise ZmbDuplicateKeyException(f"{url}")

def get_by_hash(hashed_url):
    """
    Gets an article's entities by hash
    """
    with ArticleService() as article_svc:
        return article_svc.get_articles_by_hash(hashed_url)

def get_articles_by_criteria(criteria):
    """
    Gets an article's entities by entities' value
    Args:
        criteria: the entities value such as "São Paulo"
    """
    with ArticleService() as article_svc:
        return article_svc.get_articles_by_criteria(criteria)
