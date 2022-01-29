from db.tables.tb_definitions import *
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
from zmb_labels import ZmbLabels
from sqlalchemy.sql import func
from sqlalchemy.sql import desc

class SearchType:
    NAME = "name"
    HASH = "hash"

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
        of a JSON such as {"people": ["Martin Luther King"]} or by hash such as
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

    def count_by_name(self, class_, name):
        """
        Count the number of entries for this entity
        """
        result = self._session.query(class_.name,
                                      func.count('*').label('count')) \
                                        .filter(class_.name.like(f"%{name}%")) \
                                          .group_by(class_.name) \
                                            .order_by(desc('count'))
        result_lst = []
        for row in result:
            result_lst.append({'name': row.name, 'count': row.count})
        return result_lst

    def count_by_freq(self, class_, topk=10):
        """
        Count the number of ocurrences of an entity
        """
        result = self._session.query(class_.name, \
                                        func.count('*').label('count')) \
                                            .group_by(class_.name) \
                                                .order_by(desc('count'))
        k = 0
        result_lst = []
        for row in result:
            if (k >= topk):
                break
            result_lst.append({'name': row.name, 'count': row.count})
            k += 1
        return result_lst

    def _build_return_map(self, results, entity_name):
        """
        Transform results into a map
        """
        result_map = {}
        for row in results:
            # if a hash ('3ac881ce9b0b838dadceeb5fb95bfffc') is not in result_map
            if (not row.hashed_url in result_map.keys()):
                # entity_name: e.g.: "people"
                result_map[row.hashed_url] = {entity_name: []}
                # row.name: e.g., "Martin Luther King"
                # result_map[<a hash>]["people"].append("Martin Luther King")
            result_map[row.hashed_url][entity_name].append(row.name)
        # Every entity returns a dictionary with the following format
        # {<hash>: {<entity_name>: ["entity val 1", "entity val 2"]}
        # {'001': {"people": ["Martin Luther King", "Marielle Franco"]}
        return result_map

    def __enter__(self):
        """
        On enter
        """
        return self

    def __exit__(self, *exc_info):
        """
        On exit.
        By default _commit_on_exit and _close_on_exit are initialized with False
        """
        if (self._session and self._commit_on_exit):
            try:
                self._session.commit()
            except IntegrityError as e:
                self._session.close()
                raise e
        if (self._session and self._close_on_exit):
            self._session.close()


# Articles searcher
# ==============================================================================

class ArticlesSearcher(BaseSearcher):

    def query(self, hashed_url):
        results = self._session.query(TableArticles) \
                        .filter(TableArticles.hashed_url == hashed_url)
        meta = {}
        if (results):
            meta[ZmbLabels.Article.Title.api()] = results[0].title
            meta[ZmbLabels.Article.Keyword.api()] = results[0].keywords
            meta[ZmbLabels.Article.Section.api()] = results[0].section
            meta[ZmbLabels.Article.Site.api()] = results[0].site_name
            meta[ZmbLabels.Article.Author.api()] = results[0].authors
            published_time = ""
            if (results[0].published_time):
                published_time = results[0].published_time.strftime("%Y-%m-%d")
            meta[ZmbLabels.Article.PublishedTime.api()] = published_time
            meta[ZmbLabels.Article.URL.api()] = results[0].url
        return meta

# Sources searcher
# ==============================================================================

class SourcesSearcher(BaseSearcher):

    def query(self):
        api_label = ZmbLabels.Article.Source.api()
        return super().query(api_label, TableSources)

    def count_by_name(self, name):
        return super().count_by_name(TableSources)

    def count_by_freq(self, topk=10):
        return super().count_by_freq(TableSources, topk)

# Media searcher
# ==============================================================================

class MediaSearcher(BaseSearcher):

    def query(self):
        api_label = ZmbLabels.Article.Entity.Media.api()
        return super().query(api_label, TableMedia)

    def count_by_name(self, name):
        return super().count_by_name(TableMedia, name)

    def count_by_freq(self, topk=10):
        return super().count_by_freq(TableMedia, topk)

# Movement searcher
# ==============================================================================

class MovementsSearcher(BaseSearcher):

    def query(self):
        api_label = ZmbLabels.Article.Entity.Educational.api()
        return super().query(api_label, TableEducationals)

    def count_by_name(self, name):
        return super().count_by_name(TableMovements, name)

    def count_by_freq(self, topk=10):
        return super().count_by_freq(TableMovements, topk)

# People searcher
# ==============================================================================

class PeopleSearcher(BaseSearcher):

    def query(self):
        api_label = ZmbLabels.Article.Entity.People.api()
        return super().query(api_label, TablePeople)

    def count_by_name(self, name):
        return super().count_by_name(TablePeople, name)

    def count_by_freq(self, topk=10):
        return super().count_by_freq(TablePeople, topk)

# Educational searcher
# ==============================================================================

class EducationalSearcher(BaseSearcher):

    def query(self):
        api_label = ZmbLabels.Article.Entity.Educational.api()
        return super().query(api_label, TableEducationals)

    def count_by_name(self, name):
        return super().count_by_name(TableEducationals, name)

    def count_by_freq(self, topk=10):
        return super().count_by_freq(TableEducationals, topk)

# Private searcher
# ==============================================================================

class PrivateSearcher(BaseSearcher):

    def query(self):
        api_label = ZmbLabels.Article.Entity.Private.api()
        return super().query(api_label, TablePrivates)

    def count_by_name(self, name):
        return super().count_by_name(TablePrivates, name)

    def count_by_freq(self, topk=10):
        return super().count_by_freq(TablePrivates, topk)

# Public searcher
# ==============================================================================

class PublicSearcher(BaseSearcher):

    def query(self):
        api_label = ZmbLabels.Article.Entity.Public.api()
        return super().query(api_label, TablePublics)

    def count_by_name(self, name):
        return super().count_by_name(TablePublics, name)

    def count_by_freq(self, topk=10):
        return super().count_by_freq(TablePublics, topk)

# Works searcher
# ==============================================================================

class WorksSearcher(BaseSearcher):

    def query(self):
        api_label = ZmbLabels.Article.Entity.Work.api()
        return super().query(api_label, TableWorks)

    def count_by_name(self, name):
        return super().count_by_name(TableWorks, name)

    def count_by_freq(self, topk=10):
        return super().count_by_freq(TableWorks, topk)

# Cities searcher
# ==============================================================================

class CitiesSearcher(BaseSearcher):

    def query(self):
        api_label = ZmbLabels.Article.Entity.City.api()
        return super().query(api_label, TableCities)

    def count_by_name(self, name):
        return super().count_by_name(TableCities, name)

    def count_by_freq(self, topk=10):
        return super().count_by_freq(TableCities, topk)

# State searcher
# ==============================================================================

class StatesSearcher(BaseSearcher):

    def query(self):
        api_label = ZmbLabels.Article.Entity.State.api()
        return super().query(api_label, TableStates)

    def count_by_name(self, name):
        return super().count_by_name(TableStates, name)

    def count_by_freq(self, topk=10):
        return super().count_by_freq(TableStates, topk)

# Country searcher
# ==============================================================================

class CountriesSearcher(BaseSearcher):

    def query(self):
        api_label = ZmbLabels.Article.Entity.Country.api()
        return super().query(api_label, TableCountries)

    def count_by_name(self, name):
        return super().count_by_name(TableCountries, name)

    def count_by_freq(self, topk=10):
        return super().count_by_freq(TableCountries, topk)

# Laws searcher
# ==============================================================================

class LawsSearcher(BaseSearcher):

    def query(self):
        api_label = ZmbLabels.Article.Entity.Law.api()
        return super().query(api_label, TableLaws)

    def count_by_name(self, name):
        return super().count_by_name(TableLaws, name)

    def count_by_freq(self, topk=10):
        return super().count_by_freq(TableLaws, topk)

# Polices searcher
# ==============================================================================

class PolicesSearcher(BaseSearcher):

    def query(self):
        api_label = ZmbLabels.Article.Entity.Police.api()
        return super().query(api_label, TablePolices)

    def count_by_name(self, name):
        return super().count_by_name(TablePolices, name)

    def count_by_freq(self, topk=10):
        return super().count_by_freq(TablePolices, topk)

# Political searcher
# ==============================================================================

class PoliticalSearcher(BaseSearcher):

    def query(self):
        api_label = ZmbLabels.Article.Entity.Political.api()
        return super().query(api_label, TablePoliticals)

    def count_by_name(self, name):
        return super().count_by_name(TablePoliticals, name)

    def count_by_freq(self, topk=10):
        return super().count_by_freq(TablePoliticals, topk)
