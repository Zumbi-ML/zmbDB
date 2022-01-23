from db.article_service import ArticleService
from labels import *

def test_persist_one_article_n_one_entity(session):
    """
    Test
    """
    article, entities = make_a_dummy_article(1)
    hashed_url = article['hashed_url']

    with ArticleService(session, article, entities) as article_svc:
        article_svc.persist_all()
        actual = article_svc.get_articles_by_hash(hashed_url)

    expected = {hashed_url: {SOURCES: ['src1'], MEDIA: ['med1'], MOVEMENTS: ['mov1'], PEOPLE: ['per1'], EDUCATIONAL: ['edu1'], PRIVATE: ['priv1'], PUBLIC: ['pub1'], ACTIONS: ['act1'], WORKS: ['wrk1'], CITIES: ['cit1'], STATES: ['sta1'], COUNTRIES: ['cntry1'], LAWS: ['law1'], POLICES: ['pol1']}}
    assert actual == expected


def test_get_articles_with_empty_criteria(session):
    """
    """
    criteria = {SOURCES: [], MEDIA: [], MOVEMENTS: [], PEOPLE: [], EDUCATIONAL: [], PRIVATE: [], PUBLIC: [], ACTIONS: [], WORKS: [], CITIES: [], STATES: [], COUNTRIES: [], LAWS: [], POLICES: []}
    with ArticleService(session=session) as article_svc:
        actual = article_svc.get_articles_by_criteria(criteria)
    expected = {}
    assert actual == expected

def test_get_articles_with_partial_criteria_source(session):
    """
    """
    criteria = {SOURCES: ['src1']}
    with ArticleService(session=session) as article_svc:
        actual = article_svc.get_articles_by_criteria(criteria)
    hashed_url = hash("http://domain1.com")
    expected = {hashed_url: {SOURCES: ['src1'], MEDIA: [], MOVEMENTS: [], PEOPLE: [], EDUCATIONAL: [], PRIVATE: [], PUBLIC: [], ACTIONS: [], WORKS: [], CITIES: [], STATES: [], COUNTRIES: [], LAWS: [], POLICES: []}}
    assert actual == expected

def test_get_articles_with_non_existent_criteria(session):
    """
    """
    criteria = {SOURCES: ['non_existent'],
                MEDIA: ['non_existent'],
                MOVEMENTS: ['non_existent'],
                PEOPLE: ['non_existent'],
                EDUCATIONAL: ['non_existent'],
                PRIVATE: ['non_existent'],
                PUBLIC: ['non_existent'],
                ACTIONS: ['non_existent'],
                WORKS: ['non_existent'],
                CITIES: ['non_existent'],
                STATES: ['non_existent'],
                COUNTRIES: ['non_existent'],
                LAWS: ['non_existent'],
                POLICES: ['non_existent'],
                }

    with ArticleService(session=session) as article_svc:
        actual = article_svc.get_articles_by_criteria(criteria)
    expected = {}
    assert actual == expected

# Helper functions
# =======================================================

def make_a_dummy_article(i):
    url = f"http://domain{i}.com"
    hashed_url = hash(url)
    article = {                                        \
               "url": f"{url}",                        \
               "hashed_url": hashed_url,               \
               "content": f"Content of the News {i}",  \
               "publ_date": f"2021-10-0{i}",           \
               "source": f"src{i}",                    \
               "miner": f"miner{i}"
               }
    entities = {SOURCES: [f"src{j+1}" for j in range(i)],                       \
                MEDIA: [f"med{j+1}" for j in range(i)],                         \
                MOVEMENTS: [f"mov{j+1}" for j in range(i)],                     \
                PEOPLE: [f"per{j+1}" for j in range(i)],                        \
                EDUCATIONAL: [f"edu{j+1}" for j in range(i)],                   \
                PRIVATE: [f"priv{j+1}" for j in range(i)],                      \
                PUBLIC: [f"pub{j+1}" for j in range(i)],                        \
                ACTIONS: [f"act{j+1}" for j in range(i)],                       \
                WORKS: [f"wrk{j+1}" for j in range(i)],                         \
                CITIES: [f"cit{j+1}" for j in range(i)],                        \
                STATES: [f"sta{j+1}" for j in range(i)],                        \
                COUNTRIES: [f"cntry{j+1}" for j in range(i)],                   \
                LAWS: [f"law{j+1}" for j in range(i)],                          \
                POLICES: [f"pol{j+1}" for j in range(i)],                       \
                }
    return article, entities
