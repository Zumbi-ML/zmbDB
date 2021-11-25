from db.base_service import BaseService
from db.e_map import *
from db.tables.tb_definitions import *
from db.tb_searchers.searchers import *

class ArticleService(BaseService):
    def __init__(self, article=None, entities=None):
        """
        Constructor
        """
        super().__init__()
        self._article = article
        self._entities = entities
        self._hashed_uri = None

    def get_articles_by_hash(self, hashed_uri):
        return self._search(by=SearchType.HASH, params=hashed_uri)

    def get_articles_by_criteria(self, params):
        return self._search(by=SearchType.NAME, params=params)

    # Query Methods
    # =======================================================
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

    ###########################################################################
    # Persistence Methods
    ###########################################################################
    def persist_all(self):
        """
        Persist the article and its entities into the database
        """
        self.add_article()
        self.add_entities()

    def add_article(self):
        """
        Add the article to the session
        """
        self._hashed_uri = hash(self._article['uri'])
        article = TableArticles(
                        uri = self._article['uri'],                 \
                        hashed_uri = self._hashed_uri,              \
                        content = self._article['content'],         \
                        publ_date = self._article['publ_date'],     \
                        source = self._article['source'],           \
                        miner = self._article['miner'])
        self._session.add(article)

    def add_entities(self):
        """
        Add the article entities to the session
        """
        for source in self._entities['sources']:
            self._session.add(TableSources(hashed_uri=self._hashed_uri, name=source))

        for media in self._entities['media']:
            self._session.add(TableMedia(hashed_uri=self._hashed_uri, name=media))

        for movement in self._entities['movements']:
            self._session.add(TableMovements(hashed_uri=self._hashed_uri, name=movement))

        for person in self._entities['people']:
            self._session.add(TablePeople(hashed_uri=self._hashed_uri, name=person))

        for educ_inst in self._entities['educational']:
            self._session.add(TableEducationalInstitutions(hashed_uri=self._hashed_uri, name=educ_inst))

        for priv_inst in self._entities['private']:
            self._session.add(TablePrivateInstitutions(hashed_uri=self._hashed_uri, name=priv_inst))

        for publ_inst in self._entities['public']:
            self._session.add(TablePublicInstitutions(hashed_uri=self._hashed_uri, name=publ_inst))

        for action in self._entities['actions']:
            self._session.add(TableRacistActions(hashed_uri=self._hashed_uri, name=action))

        for work in self._entities['works']:
            self._session.add(TableWorks(hashed_uri=self._hashed_uri, name=work))

        for city in self._entities['cities']:
            self._session.add(TableCities(hashed_uri=self._hashed_uri, name=city))

        for state in self._entities['states']:
            self._session.add(TableStates(hashed_uri=self._hashed_uri, name=state))

        for country in self._entities['countries']:
            self._session.add(TableCountries(hashed_uri=self._hashed_uri, name=country))

        for law in self._entities['laws']:
            self._session.add(TableLaws(hashed_uri=self._hashed_uri, title=law, code=law))

        for police in self._entities['polices']:
            self._session.add(TablePolices(hashed_uri=self._hashed_uri, name=police))

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
              , where 001 and 002 are hashed URIs.
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
                    # Creates a map for a hashed URI. E.g.,
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
