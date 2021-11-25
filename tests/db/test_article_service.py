from db.article_service import ArticleService
from db.e_map import *

def test_persist_one_article_n_one_entity(session):
    article, entities = make_a_dummy_article(1)
    hashed_uri = article['hashed_uri']

    with ArticleService(session, article, entities) as article_svc:
        article_svc.persist_all()
        actual = article_svc.get_articles_by_hash(hashed_uri)
    print(actual)
    expected = {hashed_uri: {'sources': ['src1'], 'media': ['med1'], 'movements': ['mov1'], 'people': ['per0'], 'educational': ['edu1'], 'private': ['priv1'], 'public': ['pub1'], 'actions': ['act1'], 'works': ['wrk1'], 'cities': ['cit1'], 'states': ['sta1'], 'countries': ['cntry1'], 'laws': ['law1'], 'polices': ['pol1']}}
    assert actual == expected

# Helper functions
# =======================================================

def make_a_dummy_article(i):
    uri = f"http://domain{i}.com"
    hashed_uri = hash(uri)
    article = {                                        \
               "uri": f"{uri}",                        \
               "hashed_uri": hashed_uri,               \
               "content": f"Content of the News {i}",  \
               "publ_date": f"2021-10-0{i}",           \
               "source": f"src{i}",                    \
               "miner": f"miner{i}"
               }
    entities = {SOURCES: [f"src{j+1}" for j in range(i)],                       \
                MEDIA: [f"med{j+1}" for j in range(i)],                         \
                MOVEMENTS: [f"mov{j+1}" for j in range(i)],                     \
                PEOPLE: [f"per{j}" for j in range(i)],                          \
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
