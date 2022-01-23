from db.e_map import *
from db.tables.tb_definitions import *
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
from zmb_labels import ZmbLabels

class SearchType:
    NAME = "name"
    HASH = "hash"
    CODE = "code"

class BaseSearcher(object):

    def __init__(self, session, commit_on_exit=False, close_on_exit=False):
        self._session = session
        self._commit_on_exit = commit_on_exit
        self._close_on_exit = close_on_exit

    def set_search_criteria(self, search_by, criteria):
        self._search_by = search_by
        self._criteria = criteria

    def query(self, api_label, class_):
        """
        A query can be performed in two ways: by criteria, which has the format
        of a JSON such as {"people": "Martin Luther King"} or by hash such as
        '3ac881ce9b0b838dadceeb5fb95bfffc'
        Args:
            api_label: a label such as "people", "political", "public"
            class_: The table class that can handle the request such as
                    TablePeople or TableMovements
        """
        # _search_by and criteria are defined in ArticleService
        if (self._search_by == SearchType.NAME):
            # E.g.: if "people" is not in the _criteria
            # _criteria: {"public": ["STF"]}
            if (not api_label in self._criteria.keys()):
                return None

            # _criteria takes the form of a JSON in this mode
            # {"public": ["STF","IBGE"]}
            params = self._criteria[api_label]
            if (not params):
                return None

            filter_group = [class_.name.like(f"%{name}%") for name in params]
            results = self._session.query(class_).filter(or_(*filter_group))

        elif (self._search_by == SearchType.HASH):
            # _criteria takes the form of a string, a hash:
            # _criteria: ''3ac881ce9b0b838dadceeb5fb95bfffc''
            params = self._criteria
            results = self._session.query(class_).filter(class_.hashed_url == params)

        return self._build_return_map(results, api_label)

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
            if (not row.hashed_url in result_map.keys()):
                result_map[row.hashed_url] = {entity_name: []}
            result_map[row.hashed_url][entity_name].append(row.name)
        return result_map

    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        if (self._session and self._commit_on_exit):
            try:
                self._session.commit()
            except IntegrityError as e:
                self._session.close()
                raise e
        if (self._session and self._close_on_exit):
            self._session.close()


# Sources searcher
# ==============================================================================

class SourcesSearcher(BaseSearcher):

    def query(self):
        api_label = ZmbLabels.Article.Source.api()
        return super().query(api_label, TableSources)

    def count(self):
        """
        Count the number of entries for this entity
        """
        return self._session.query(TableSources.name) \
                                            .group_by(TableSources.name).count()

# Media searcher
# ==============================================================================

class MediaSearcher(BaseSearcher):

    def query(self):
        api_label = ZmbLabels.Article.Entity.Media.api()
        return super().query(api_label, TableMedia)

    def count(self):
        """
        Count the number of entries for this entity
        """
        return self._session.query(TableMedia.name) \
                                            .group_by(TableMedia.name).count()

# Movement searcher
# ==============================================================================

class MovementsSearcher(BaseSearcher):

    def query(self):
        api_label = ZmbLabels.Article.Entity.Educational.api()
        return super().query(api_label, TableEducationals)

    def count(self):
        """
        Count the number of entries for this entity
        """
        return self._session.query(TableMovements.name) \
                                          .group_by(TableMovements.name).count()

# People searcher
# ==============================================================================

class PeopleSearcher(BaseSearcher):

    def query(self):
        api_label = ZmbLabels.Article.Entity.People.api()
        return super().query(api_label, TablePeople)

    def count(self):
        """
        Count the number of entries for this entity
        """
        return self._session.query(TablePeople.name) \
                                            .group_by(TablePeople.name).count()

# Educational searcher
# ==============================================================================

class EducationalSearcher(BaseSearcher):

    def query(self):
        api_label = ZmbLabels.Article.Entity.Educational.api()
        return super().query(api_label, TableEducationals)

    def count(self):
        """
        Count the number of entries for this entity
        """
        return self._session.query(TableEducationals.name) \
                            .group_by(TableEducationals.name).count()

# Private searcher
# ==============================================================================

class PrivateSearcher(BaseSearcher):

    def query(self):
        api_label = ZmbLabels.Article.Entity.Private.api()
        return super().query(api_label, TablePrivates)

    def count(self):
        """
        Count the number of entries for this entity
        """
        return self._session.query(TablePrivates.name) \
                                .group_by(TablePrivates.name).count()

# Public searcher
# ==============================================================================

class PublicSearcher(BaseSearcher):

    def query(self):
        api_label = ZmbLabels.Article.Entity.Public.api()
        return super().query(api_label, TablePublics)

    def count(self):
        """
        Count the number of entries for this entity
        """
        return self._session.query(TablePublics.name) \
                                .group_by(TablePublics.name).count()

# Works searcher
# ==============================================================================

class WorksSearcher(BaseSearcher):

    def query(self):
        api_label = ZmbLabels.Article.Entity.Work.api()
        return super().query(api_label, TableWorks)

    def count(self):
        """
        Count the number of entries for this entity
        """
        return self._session.query(TableWorks.name) \
                                .group_by(TableWorks.name).count()

# Cities searcher
# ==============================================================================

class CitiesSearcher(BaseSearcher):

    def query(self):
        api_label = ZmbLabels.Article.Entity.City.api()
        return super().query(api_label, TableCities)

    def count(self):
        """
        Count the number of entries for this entity
        """
        return self._session.query(TableCities.name) \
                                .group_by(TableCities.name).count()

# State searcher
# ==============================================================================

class StatesSearcher(BaseSearcher):

    def query(self):
        api_label = ZmbLabels.Article.Entity.State.api()
        return super().query(api_label, TableStates)

    def count(self):
        """
        Count the number of entries for this entity
        """
        return self._session.query(TableStates.name) \
                                .group_by(TableStates.name).count()

# Country searcher
# ==============================================================================

class CountriesSearcher(BaseSearcher):

    def query(self):
        api_label = ZmbLabels.Article.Entity.Country.api()
        return super().query(api_label, TableCountries)

    def count(self):
        """
        Count the number of entries for this entity
        """
        return self._session.query(TableCountries.name) \
                                          .group_by(TableCountries.name).count()

# Laws searcher
# ==============================================================================

class LawsSearcher(BaseSearcher):

    def query(self):
        api_label = ZmbLabels.Article.Entity.Law.api()
        return super().query(api_label, TableLaws)

    def count(self):
        """
        Count the number of entries for this entity
        """
        return self._session.query(TableLaws.title) \
                                              .group_by(TableLaws.title).count()

# Polices searcher
# ==============================================================================

class PolicesSearcher(BaseSearcher):

    def query(self):
        api_label = ZmbLabels.Article.Entity.Police.api()
        return super().query(api_label, TablePolices)

    def count(self):
        """
        Count the number of entries for this entity
        """
        return self._session.query(TablePolices.name) \
                                .group_by(TablePolices.name).count()

# Political searcher
# ==============================================================================

class PoliticalSearcher(BaseSearcher):

    def query(self):
        api_label = ZmbLabels.Article.Entity.Political.api()
        return super().query(api_label, TablePoliticals)

    def count(self):
        """
        Count the number of entries for this entity
        """
        return self._session.query(TablePolices.name) \
                                .group_by(TablePolices.name).count()
