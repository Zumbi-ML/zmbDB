from db.base_service import BaseService
from labels import *
from db.tables.tb_definitions import *
from db.tb_searchers.searchers import *
from datetime import date

class ArticleService(BaseService):
    def __init__(self, session=None, commit_on_exit=True, close_on_exit=True):
        """
        Constructor
        """
        super().__init__(session=session, commit_on_exit=commit_on_exit, close_on_exit=close_on_exit)
        self._hashed_url = None

    def get_articles_by_hash(self, hashed_url):
        return self._search(by=SearchType.HASH, params=hashed_url)

    def get_articles_by_criteria(self, params):
        return self._search(by=SearchType.NAME, params=params)

    # Query Methods
    # ==========================================================================
    def _search(self, by, params):
        maps = []

        with SourcesSearcher(self._session) as searcher:
            searcher.set_search_criteria(by, params)
            result = searcher.query()
            if (result):
                maps.append(result)

        with MediaSearcher(self._session) as searcher:
            searcher.set_search_criteria(by, params)
            result = searcher.query()
            if (result):
                maps.append(result)

        with MovementsSearcher(self._session) as searcher:
            searcher.set_search_criteria(by, params)
            result = searcher.query()
            if (result):
                maps.append(result)

        with PeopleSearcher(self._session) as searcher:
            searcher.set_search_criteria(by, params)
            result = searcher.query()
            if (result):
                maps.append(result)

        with EducationalSearcher(self._session) as searcher:
            searcher.set_search_criteria(by, params)
            result = searcher.query()
            if (result):
                maps.append(result)

        with PrivateSearcher(self._session) as searcher:
            searcher.set_search_criteria(by, params)
            result = searcher.query()
            if (result):
                maps.append(result)

        with PublicSearcher(self._session) as searcher:
            searcher.set_search_criteria(by, params)
            result = searcher.query()
            if (result):
                maps.append(result)

        with ActionsSearcher(self._session) as searcher:
            searcher.set_search_criteria(by, params)
            result = searcher.query()
            if (result):
                maps.append(result)

        with WorksSearcher(self._session) as searcher:
            searcher.set_search_criteria(by, params)
            result = searcher.query()
            if (result):
                maps.append(result)

        with CitiesSearcher(self._session) as searcher:
            searcher.set_search_criteria(by, params)
            result = searcher.query()
            if (result):
                maps.append(result)

        with StatesSearcher(self._session) as searcher:
            searcher.set_search_criteria(by, params)
            result = searcher.query()
            if (result):
                maps.append(result)

        with CountriesSearcher(self._session) as searcher:
            searcher.set_search_criteria(by, params)
            result = searcher.query()
            if (result):
                maps.append(result)

        with LawsSearcher(self._session) as searcher:
            if (by == SearchType.NAME):
                by_law = SearchType.TITLE
            elif (by == SearchType.HASH):
                by_law = SearchType.HASH
            searcher.set_search_criteria(by_law, params)
            result = searcher.query()
            if (result):
                maps.append(result)

        with PolicesSearcher(self._session) as searcher:
            searcher.set_search_criteria(by, params)
            result = searcher.query()
            if (result):
                maps.append(result)

        return self._build_return_map(maps)

    # Persistence Methods
    # ==========================================================================

    def persist_article_n_entities(self, article_map):
        """
        Persist an article and its entities
        """
        self._hashed_url = article_map['hashed_url']
        entities_map = article_map[ENTITIES]
        self.add_article(article_map)
        self.add_entities(entities_map)

    def persist_all(self):
        """
        Persist the article and its entities into the database
        """
        self.add_article()
        self.add_entities()

    def add_article(self, article_map):
        """
        Adds the article_map to the session
        """

        article = TableArticles(
                    hashed_url = self._hashed_url,
                    url = article_map[URL],
                    content = article_map[CONTENT],
                    published_time=article_map[PUBLISHED_TIME],
                    title=article_map[TITLE],
                    keywords=article_map[KEYWORDS],
                    section=article_map[SECTION],
                    site_name=article_map[SITE_NAME],
                    authors=article_map[AUTHORS],
                    miner = article_map[MINER],
                    source = article_map[SOURCE],
                    added = date.today(),
                    last_modified = date.today(),)
        self._session.add(article)

    def add_entities(self, entities_map):
        """
        Add the article entities to the session
        """

        if (MEDIA in entities_map.keys()):
            for media in entities_map[MEDIA]:
                self._session.add(TableMedia(hashed_url=self._hashed_url, name=media))

        if (MOVEMENTS in entities_map.keys()):
            for movement in entities_map[MOVEMENTS]:
                self._session.add(TableMovements(hashed_url=self._hashed_url, name=movement))

        if (PEOPLE in entities_map.keys()):
            for person in entities_map[PEOPLE]:
                self._session.add(TablePeople(hashed_url=self._hashed_url, name=person))

        if (EDUCATIONAL in entities_map.keys()):
            for educ_inst in entities_map[EDUCATIONAL]:
                self._session.add(TableEducationalInstitutions(hashed_url=self._hashed_url, name=educ_inst))

        if (PRIVATE in entities_map.keys()):
            for priv_inst in entities_map[PRIVATE]:
                self._session.add(TablePrivateInstitutions(hashed_url=self._hashed_url, name=priv_inst))

        if (PUBLIC in entities_map.keys()):
            for publ_inst in entities_map[PUBLIC]:
                self._session.add(TablePublicInstitutions(hashed_url=self._hashed_url, name=publ_inst))

        if (ACTIONS in entities_map.keys()):
            for action in entities_map[ACTIONS]:
                self._session.add(TableRacistActions(hashed_url=self._hashed_url, name=action))

        if (WORKS in entities_map.keys()):
            for work in entities_map[WORKS]:
                self._session.add(TableWorks(hashed_url=self._hashed_url, name=work))

        if (CITIES in entities_map.keys()):
            for city in entities_map[CITIES]:
                self._session.add(TableCities(hashed_url=self._hashed_url, name=city))

        if (STATES in entities_map.keys()):
            for state in entities_map[STATES]:
                self._session.add(TableStates(hashed_url=self._hashed_url, name=state))

        if (COUNTRIES in entities_map.keys()):
            for country in entities_map[COUNTRIES]:
                self._session.add(TableCountries(hashed_url=self._hashed_url, name=country))

        if (LAWS in entities_map.keys()):
            for law in entities_map[LAWS]:
                self._session.add(TableLaws(hashed_url=self._hashed_url, title=law, code=law))

        if (POLICES in entities_map.keys()):
            for police in entities_map[POLICES]:
                self._session.add(TablePolices(hashed_url=self._hashed_url, name=police))

    def _build_return_map(self, input_maps):
        """
        Combines all result rows into a coherent dict
        Args: input_maps:
              A list of dictionaries.
              E.g.:
              [
                {001: {'sources': 'src1'}, 002: {'sources': 'src2'}},
                {001: {'media': 'med1'}},
                {002: {'people': 'p2'}},
              ]
              , where 001 and 002 are hashed urls.
        Return
            output_map
            {
                001: {'sources': ['src1'], 'media': ['med1'], 'people': []...},
                002: {'sources': ['src2'], 'media': [], 'people': ['p2']}
            }
        """
        output_map = {}
        # E.g.
        # {001: {'sources': 'src1'}, 002: {'sources': 'src2'}}
        for input_map in input_maps:
            # hash_: 001
            for hash_ in input_map.keys():
                if (not hash_ in output_map.keys()):
                    # Creates a map for a hashed url. E.g.,
                    # {001: {} }
                    output_map[hash_] = {}
                # E.g.
                # 'sources'
                for entity_ in input_map[hash_]:
                    # Obtains the values for an entity
                    # {001: {'sources': ['src1']} => ['src1']
                    elements_lst = input_map[hash_][entity_]
                    # {001: {'sources': ['src1']}}
                    output_map[hash_][entity_] = elements_lst

        # Fill in missing entities
        # E.g.
        # hash_: 001
        for hash_ in output_map.keys():
            # E.g.
            # entity_: sources
            for entity_ in ALL_ENTITIES:
                # if an entity_ is not in the output_map
                if (not entity_ in output_map[hash_].keys()):
                    # Creates an entry with an empty list in output_map
                    output_map[hash_][entity_] = []
        return output_map
