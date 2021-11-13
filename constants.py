from db.tables.tb_definitions import *

SUCCESSFUL = 200
UNAUTHORIZED = 401

"""
entities_map = {
    "source": TableSources,
    "media": TableMedia,
    "movement": TableMovements,
    "people": TablePeople,
    "educational": TableEducationalInstitutions,
    "private": TablePrivateInstitutions,
    "public": TablePublicInstitutions,
    "actions": TableRacistActions,
    "city": TableCities,
    "state": TableStates,
    "country": TableCountries,
    "work": TableWorks,
    "police": TablePolices,
    "law": TableLaws,
    "text": TableArticles,
}
"""

API_KEY_SIZE = 32
PERM_LEVEL = {
    "demo": 0,
    "basic": 1,
    "researcher": 2,
    "app": 3,
    "admin": 4,
}
