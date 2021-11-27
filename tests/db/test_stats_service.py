from db.stats_service import StatsService
from db.e_map import *

def test_count_entities(session):
    """
    Test the count of all entities per entity type
    """
    with StatsService(session) as service:
        actual = service.count_entities()
    expected = {SOURCES: 1, MEDIA: 1, MOVEMENTS: 1, PEOPLE: 1, EDUCATIONAL: 1, PRIVATE: 1, PUBLIC: 1, ACTIONS: 1, CITIES: 1, STATES: 1, COUNTRIES: 1, WORKS: 1, POLICES: 1, LAWS: 1}
    assert actual == expected
