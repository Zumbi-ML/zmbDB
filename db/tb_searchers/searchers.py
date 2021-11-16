from db.e_map import *
from db.tables.tb_definitions import *
from sqlalchemy import or_

class BaseSearcher(object):

    def __init__(self, session, commit_on_exit=False, close_on_exit=False):
        self._session = session
        self._commit_on_exit = commit_on_exit
        self._close_on_exit = close_on_exit

    def query(self, attribute_lst, by=None):
        msg = \
        """
        This is an abstract class.
        Please instantiate one of its subclasses instead.
        """
        raise NotImplementedError(msg)

    def _build_return_map(self, results, entity_name):
        result_map = {}
        for row in results:
            result_map[row.hashed_uri] = {entity_name: row.name}
        return result_map

    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        if (self._session and self._commit_on_exit):
            self._session.commit()
        if (self._session and self._close_on_exit):
            self._session.close()

class SourcesSearcher(BaseSearcher):
    def query(self, attribute_lst, by="name"):
        filter_group = [TableSources.name.like(f"%{name}%") for name in attribute_lst]
        results = self._session.query(TableSources).filter(or_(*filter_group))
        return self._build_return_map(results, SOURCES)

class MediaSearcher(BaseSearcher):
    def query(self, attribute_lst, by="name"):
        filter_group = [TableMedia.name.like(f"%{name}%") for name in attribute_lst]
        results = self._session.query(TableMedia).filter(or_(*filter_group))
        return self._build_return_map(results, MEDIA)

class MovementsSearcher(BaseSearcher):
    def query(self, attribute_lst, by="name"):
        filter_group = [TableMovements.name.like(f"%{name}%") for name in attribute_lst]
        results = self._session.query(TableMovements).filter(or_(*filter_group))
        return self._build_return_map(results, MOVEMENTS)

class PeopleSearcher(BaseSearcher):
    def query(self, attribute_lst, by="name"):
        filter_group = [TablePeople.name.like(f"%{name}%") for name in attribute_lst]
        results = self._session.query(TablePeople).filter(or_(*filter_group))
        return self._build_return_map(results, PEOPLE)

class EducationalSearcher(BaseSearcher):
    def query(self, attribute_lst, by="name"):
        filter_group = [TableEducationalInstitutions.name.like(f"%{name}%")           \
                                                    for name in attribute_lst]
        results = self._session.query(TableEducationalInstitutions)    \
                                                    .filter(or_(*filter_group))
        return self._build_return_map(results, EDUCATIONAL)

class PrivateSearcher(BaseSearcher):
    def query(self, attribute_lst, by="name"):
        filter_group = [TablePrivateInstitutions.name.like(f"%{name}%")            \
                                                    for name in attribute_lst]
        results = self._session.query(TablePrivateInstitutions)                \
                                                    .filter(or_(*filter_group))
        return self._build_return_map(results, PRIVATE)

class PublicSearcher(BaseSearcher):
    def query(self, attribute_lst, by="name"):
        filter_group = [TablePublicInstitutions.name.like(f"%{name}%")                \
                                                    for name in attribute_lst]
        results = self._session.query(TablePublicInstitutions)                    \
                                                    .filter(or_(*filter_group))
        return self._build_return_map(results, PUBLIC)

class ActionsSearcher(BaseSearcher):
    def query(self, attribute_lst, by="name"):
        filter_group = [TableRacistActions.name.like(f"%{name}%")                     \
                                                    for name in attribute_lst]
        results = self._session.query(TableRacistActions).filter(or_(*filter_group))
        return self._build_return_map(results, ACTIONS)

class WorksSearcher(BaseSearcher):
    def query(self, attribute_lst, by="name"):
        filter_group = [TableWorks.name.like(f"%{name}%") for name in attribute_lst]
        results = self._session.query(TableWorks).filter(or_(*filter_group))
        return self._build_return_map(results, WORKS)

class CitiesSearcher(BaseSearcher):
    def query(self, attribute_lst, by="name"):
        filter_group = [TableCities.name.like(f"%{name}%") for name in attribute_lst]
        results = self._session.query(TableCities).filter(or_(*filter_group))
        return self._build_return_map(results, CITIES)

class StatesSearcher(BaseSearcher):
    def query(self, attribute_lst, by="name"):
        filter_group = [TableStates.name.like(f"%{name}%") for name in attribute_lst]
        results = self._session.query(TableStates).filter(or_(*filter_group))
        return self._build_return_map(results, STATES)

class CountriesSearcher(BaseSearcher):
    def query(self, attribute_lst, by="name"):
        filter_group = [TableCountries.name.like(f"%{name}%") for name in attribute_lst]
        results = self._session.query(TableCountries).filter(or_(*filter_group))
        return self._build_return_map(results, COUNTRIES)

class LawsSearcher(BaseSearcher):
    def query(self, attribute_lst, by="title"):
        filter_group = [TableLaws.title.like(f"%{title}%") for title in attribute_lst]
        results = self._session.query(TableLaws).filter(or_(*filter_group))
        result_map = {}
        for row in results:
            result_map[row.hashed_uri] = {LAWS: row.title}
        return result_map

class PolicesSearcher(BaseSearcher):
    def query(self, attribute_lst, by="name"):
        filter_group = [TablePolices.name.like(f"%{name}%") for name in attribute_lst]
        results = self._session.query(TablePolices).filter(or_(*filter_group))
        return self._build_return_map(results, POLICES)
