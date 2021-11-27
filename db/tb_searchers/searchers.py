from db.e_map import *
from db.tables.tb_definitions import *
from sqlalchemy import or_

class SearchType:
    NAME = "name"
    HASH = "hash"
    TITLE = "title"

class BaseSearcher(object):

    def __init__(self, session, commit_on_exit=False, close_on_exit=False):
        self._session = session
        self._commit_on_exit = commit_on_exit
        self._close_on_exit = close_on_exit

    def set_search_criteria(self, search_by, criteria):
        self._search_by = search_by
        self._criteria = criteria

    def query(self):
        msg = \
        """
        This is an abstract class.
        Please instantiate one of its subclasses instead.
        """
        raise NotImplementedError(msg)

    def count(self):
        msg = \
        """
        This is an abstract class.
        Please instantiate one of its subclasses instead.
        """
        raise NotImplementedError(msg)

    def _build_return_map(self, results, entity_name):
        result_map = {}
        for row in results:
            if (not row.hashed_uri in result_map.keys()):
                result_map[row.hashed_uri] = {entity_name: []}
            result_map[row.hashed_uri][entity_name].append(row.name)
        return result_map

    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        if (self._session and self._commit_on_exit):
            self._session.commit()
        if (self._session and self._close_on_exit):
            self._session.close()

# Subclasses
# =======================================================

class SourcesSearcher(BaseSearcher):

    def query(self):
        """
        """
        if (self._search_by == SearchType.NAME):
            if (not SOURCES in self._criteria.keys()):
                return None

            params = self._criteria[SOURCES]
            if (not params):
                return None

            filter_group = [TableSources.name.like(f"%{name}%") for name in params]
            results = self._session.query(TableSources).filter(or_(*filter_group))

        elif (self._search_by == SearchType.HASH):
            params = self._criteria
            results = self._session.query(TableSources)                        \
                                  .filter(TableSources.hashed_uri == params)

        return self._build_return_map(results, SOURCES)

    def count(self):
        """
        Count the number of entries for this entity
        """

        return self._session.query(TableSources.name)                          \
                                            .group_by(TableSources.name).count()


class MediaSearcher(BaseSearcher):

    def query(self):
        """
        """
        if (self._search_by == SearchType.NAME):
            if (not MEDIA in self._criteria.keys()):
                return None

            params = self._criteria[MEDIA]
            if (not params):
                return None

            filter_group = [TableMedia.name.like(f"%{name}%") for name in params]
            results = self._session.query(TableMedia).filter(or_(*filter_group))

        elif (self._search_by == SearchType.HASH):
            params = self._criteria
            results = self._session.query(TableMedia)                          \
                                    .filter(TableMedia.hashed_uri == params).all()

        return self._build_return_map(results, MEDIA)

    def count(self):
        """
        Count the number of entries for this entity
        """


        return self._session.query(TableMedia.name)                            \
                                            .group_by(TableMedia.name).count()


class MovementsSearcher(BaseSearcher):

    def query(self):
        """
        """
        if (self._search_by == SearchType.NAME):
            if (not MOVEMENTS in self._criteria.keys()):
                return None

            params = self._criteria[MOVEMENTS]
            if (not params):
                return None

            filter_group = [TableMovements.name.like(f"%{name}%") for name in params]
            results = self._session.query(TableMovements).filter(or_(*filter_group))

        elif (self._search_by == SearchType.HASH):
            params = self._criteria
            results = self._session.query(TableMovements)                      \
                                .filter(TableMovements.hashed_uri == params)

        return self._build_return_map(results, MOVEMENTS)

    def count(self):
        """
        Count the number of entries for this entity
        """

        return self._session.query(TableMovements.name)                        \
                                          .group_by(TableMovements.name).count()


class PeopleSearcher(BaseSearcher):

    def query(self):

        if (self._search_by == SearchType.NAME):
            if (not PEOPLE in self._criteria.keys()):
                return None

            params = self._criteria[PEOPLE]
            if (not params):
                return None

            filter_group = [TablePeople.name.like(f"%{name}%") for name in params]
            results = self._session.query(TablePeople).filter(or_(*filter_group))

        elif (self._search_by == SearchType.HASH):
            params = self._criteria
            results = self._session.query(TablePeople)                         \
                                   .filter(TablePeople.hashed_uri == params)

        return self._build_return_map(results, PEOPLE)

    def count(self):
        """
        Count the number of entries for this entity
        """

        return self._session.query(TablePeople.name)                           \
                                            .group_by(TablePeople.name).count()


class EducationalSearcher(BaseSearcher):

    def query(self):
        """
        """
        if (self._search_by == SearchType.NAME):
            if (not EDUCATIONAL in self._criteria.keys()):
                return None

            params = self._criteria[EDUCATIONAL]
            if (not params):
                return None

            filter_group = [TableEducationalInstitutions.name.like(f"%{name}%") \
                                                        for name in params]
            results = self._session.query(TableEducationalInstitutions)        \
                                                     .filter(or_(*filter_group))

        elif (self._search_by == SearchType.HASH):
            params = self._criteria
            results = self._session.query(TableEducationalInstitutions)        \
                  .filter(TableEducationalInstitutions.hashed_uri == params)

        return self._build_return_map(results, EDUCATIONAL)

    def count(self):
        """
        Count the number of entries for this entity
        """

        return self._session.query(TableEducationalInstitutions.name)          \
                            .group_by(TableEducationalInstitutions.name).count()


class PrivateSearcher(BaseSearcher):

    def query(self):
        if (self._search_by == SearchType.NAME):
            if (not PRIVATE in self._criteria.keys()):
                return None

            params = self._criteria[PRIVATE]
            if (not params):
                return None

            filter_group = [TablePrivateInstitutions.name.like(f"%{name}%")    \
                                                        for name in params]
            results = self._session.query(TablePrivateInstitutions)            \
                                                    .filter(or_(*filter_group))

        elif (self._search_by == SearchType.HASH):
            params = self._criteria
            results = self._session.query(TablePrivateInstitutions)            \
                        .filter(TablePrivateInstitutions.hashed_uri == params)

        return self._build_return_map(results, PRIVATE)

    def count(self):
        """
        Count the number of entries for this entity
        """

        return self._session.query(TablePrivateInstitutions.name)              \
                                .group_by(TablePrivateInstitutions.name).count()


class PublicSearcher(BaseSearcher):

    def query(self):
        if (self._search_by == SearchType.NAME):
            if (not PUBLIC in self._criteria.keys()):
                return None

            params = self._criteria[PUBLIC]
            if (not params):
                return None

            filter_group = [TablePublicInstitutions.name.like(f"%{name}%")         \
                                                        for name in params]
            results = self._session.query(TablePublicInstitutions)              \
                                                        .filter(or_(*filter_group))

        elif (self._search_by == SearchType.HASH):
            params = self._criteria
            results = self._session.query(TablePublicInstitutions)             \
                                    .filter(TablePublicInstitutions.hashed_uri == params)

        return self._build_return_map(results, PUBLIC)

    def count(self):
        """
        Count the number of entries for this entity
        """

        return self._session.query(TablePublicInstitutions.name)               \
                                .group_by(TablePublicInstitutions.name).count()


class ActionsSearcher(BaseSearcher):

    def query(self):
        if (self._search_by == SearchType.NAME):

            if (not ACTIONS in self._criteria.keys()):
                return None

            params = self._criteria[ACTIONS]
            if (not params):
                return None

            filter_group = [TableRacistActions.name.like(f"%{name}%")          \
                                                        for name in params]
            results = self._session.query(TableRacistActions).filter(or_(*filter_group))

        elif (self._search_by == SearchType.HASH):
            params = self._criteria
            results = self._session.query(TableRacistActions)                  \
                            .filter(TableRacistActions.hashed_uri == params)

        return self._build_return_map(results, ACTIONS)

    def count(self):
        """
        Count the number of entries for this entity
        """

        return self._session.query(TableRacistActions.name)                    \
                                .group_by(TableRacistActions.name).count()


class WorksSearcher(BaseSearcher):

    def query(self):
        if (self._search_by == SearchType.NAME):

            if (not WORKS in self._criteria.keys()):
                return None

            params = self._criteria[WORKS]
            if (not params):
                return None

            filter_group = [TableWorks.name.like(f"%{name}%") for name in params]
            results = self._session.query(TableWorks).filter(or_(*filter_group))


        elif (self._search_by == SearchType.HASH):
            params = self._criteria
            results = self._session.query(TableWorks)                          \
                                    .filter(TableWorks.hashed_uri == params)

        return self._build_return_map(results, WORKS)

    def count(self):
        """
        Count the number of entries for this entity
        """

        return self._session.query(TableWorks.name)         \
                                .group_by(TableWorks.name).count()


class CitiesSearcher(BaseSearcher):

    def query(self):

        if (self._search_by == SearchType.NAME):

            if (not CITIES in self._criteria.keys()):
                return None

            params = self._criteria[CITIES]
            if (not params):
                return None

            filter_group = [TableCities.name.like(f"%{name}%") for name in params]
            results = self._session.query(TableCities)                         \
                                                     .filter(or_(*filter_group))

        elif (self._search_by == SearchType.HASH):
            params = self._criteria
            results = self._session.query(TableCities)                         \
                                   .filter(TableCities.hashed_uri == params)

        return self._build_return_map(results, CITIES)

    def count(self):
        """
        Count the number of entries for this entity
        """

        return self._session.query(TableCities.name)                           \
                                .group_by(TableCities.name).count()


class StatesSearcher(BaseSearcher):

    def query(self):
        if (self._search_by == SearchType.NAME):

            if (not STATES in self._criteria.keys()):
                return None

            params = self._criteria[STATES]
            if (not params):
                return None

            filter_group = [TableStates.name.like(f"%{name}%") for name in params]
            results = self._session.query(TableStates).filter(or_(*filter_group))

        elif (self._search_by == SearchType.HASH):
            params = self._criteria
            results = self._session.query(TableStates)                         \
                                   .filter(TableStates.hashed_uri == params)

        return self._build_return_map(results, STATES)

    def count(self):
        """
        Count the number of entries for this entity
        """

        return self._session.query(TableStates.name)                           \
                                .group_by(TableStates.name).count()


class CountriesSearcher(BaseSearcher):

    def query(self):
        if (self._search_by == SearchType.NAME):

            if (not COUNTRIES in self._criteria.keys()):
                return None

            params = self._criteria[COUNTRIES]
            if (not params):
                return None

            filter_group = [TableCountries.name.like(f"%{name}%") for name in params]
            results = self._session.query(TableCountries)                      \
                                                     .filter(or_(*filter_group))

        elif (self._search_by == SearchType.HASH):
            params = self._criteria
            results = self._session.query(TableCountries)                      \
                                .filter(TableCountries.hashed_uri == params)

        return self._build_return_map(results, COUNTRIES)

    def count(self):
        """
        Count the number of entries for this entity
        """

        return self._session.query(TableCountries.name)                        \
                                          .group_by(TableCountries.name).count()


class LawsSearcher(BaseSearcher):

    def query(self):
        if (self._search_by == SearchType.TITLE):

            if (not LAWS in self._criteria.keys()):
                return None

            params = self._criteria[LAWS]
            if (not params):
                return None

            filter_group = [TableLaws.title.like(f"%{title}%") for title in params]
            results = self._session.query(TableLaws).filter(or_(*filter_group))

        elif (self._search_by == SearchType.HASH):
            params = self._criteria
            results = self._session.query(TableLaws)                           \
                                     .filter(TableLaws.hashed_uri == params)

        result_map = {}
        for row in results:
            result_map[row.hashed_uri] = {LAWS: [row.title]}
        return result_map

    def count(self):
        """
        Count the number of entries for this entity
        """

        return self._session.query(TableLaws.title)                            \
                                              .group_by(TableLaws.title).count()


class PolicesSearcher(BaseSearcher):

    def query(self):
        """
        """

        if (self._search_by == SearchType.NAME):

            if (not POLICES in self._criteria.keys()):
                return None

            params = self._criteria[POLICES]
            if (not params):
                return None

            filter_group = [TablePolices.name.like(f"%{name}%") for name in params]
            results = self._session.query(TablePolices).filter(or_(*filter_group))


        elif (self._search_by == SearchType.HASH):
            params = self._criteria
            results = self._session.query(TablePolices)                        \
                                  .filter(TablePolices.hashed_uri == params)

        return self._build_return_map(results, POLICES)

    def count(self):
        """
        Count the number of entries for this entity
        """

        return self._session.query(TablePolices.name)                          \
                                .group_by(TablePolices.name).count()
