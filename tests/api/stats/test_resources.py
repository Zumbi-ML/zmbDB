# encoding: utf-8
import json
from db.e_map import *


def test_stats_count_entities(client_session):
    """
    Test routing for counting all entities per entity type
    """
    client, session = client_session
    route = "/api/v1/stats/count/entities"
    response = client.get(route)
    assert response.status_code == 200
    #expected = {SOURCES: 1, MEDIA: 1, MOVEMENTS: 1, PEOPLE: 1, EDUCATIONAL: 1, PRIVATE: 1, PUBLIC: 1, ACTIONS: 1, CITIES: 1, STATES: 1, COUNTRIES: 1, WORKS: 1, POLICES: 1, LAWS: 1}
    #actual = json.loads(response.get_data(as_text=True))
    #assert actual == expected
