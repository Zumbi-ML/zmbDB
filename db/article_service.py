from db.base_service import BaseService
from db.tables.tb_definitions import *
from db.tb_searchers.searchers import *
from datetime import date
from zmb_labels import ZmbLabels

class ArticleService(BaseService):

    def __init__(self, session=None, commit_on_exit=True, close_on_exit=True):
        """
        Constructor
        """
        super().__init__(session=session, commit_on_exit=commit_on_exit, close_on_exit=close_on_exit)
        self._hashed_url = None

    def get_articles_by_hash(self, hashed_url):
        """
        Get article's by hash
        """
        return self._search(by=SearchType.HASH, params=hashed_url)

    def get_articles_by_criteria(self, params):
        """
        Get article's by the entities' values. E.g., all entities that matches
        the criteria 'São Paulo', which could be the name of a city or be part
        of the name of a university and so on
        """
        return self._search(by=SearchType.NAME, params=params)

    def _all_searchers(self):
        """
        Returns the searchers for entities and relevant meta information
        about the article such as Sources
        """
        return [SourcesSearcher(self._session),
                MediaSearcher(self._session),
                MovementsSearcher(self._session),
                PeopleSearcher(self._session),
                EducationalSearcher(self._session),
                PrivateSearcher(self._session),
                PublicSearcher(self._session),
                WorksSearcher(self._session),
                CitiesSearcher(self._session),
                StatesSearcher(self._session),
                CountriesSearcher(self._session),
                #LawsSearcher(self._session),
                LawsSearcher(self._session),
                PolicesSearcher(self._session),
                PoliticalSearcher(self._session),
                #ActionsSearcher(self._session),
                ]

    def _search(self, by, params):
        """
        Invoke each searcher for a query
        """
        maps = []

        for searcher in self._all_searchers():
            searcher.set_search_criteria(by, params)
            result = searcher.query()
            if (result):
                maps.append(result)

        return self._build_return_map(maps)

    def persist_article_n_entities(self, article_map):
        """
        Persist an article and its entities
        """
        self._hashed_url = article_map['hashed_url']

        entities_lbl = ZmbLabels.Article.Entity.api()
        entities_map = article_map[entities_lbl]

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
                    url = article_map[ZmbLabels.Article.URL.api()],
                    content = article_map[ZmbLabels.Article.Content.api()],
                    published_time = article_map[ZmbLabels.Article.PublishedTime.api()],
                    title = article_map[ZmbLabels.Article.Title.api()],
                    keywords = article_map[ZmbLabels.Article.Keyword.api()],
                    section = article_map[ZmbLabels.Article.Section.api()],
                    site_name = article_map[ZmbLabels.Article.Site.api()],
                    authors = article_map[ZmbLabels.Article.Author.api()],
                    html = article_map[ZmbLabels.Article.HTML.api()],
                    meta_data = article_map[ZmbLabels.Article.Metadata.api()],
                    miner = article_map[ZmbLabels.Article.Miner.api()],
                    added = date.today(),
                    last_modified = date.today(),)
        self._session.add(article)

    def add_entities(self, entities_map):
        """
        Add the article entities to the session
        """
        # E.g., label = "people"
        for label in ZmbLabels.Article.Entity.all_labels_n_metainfo():
            # If "people" is present in the map and entities["people"] is valid
            if (label in entities_map.keys() and entities_map[label]):
                # E.g., entity_name = "Martin Luther King Jr."
                for entity_name in entities_map[label]:
                    # Loads a mapping (each time it creates a different obj)
                    table_mapping = self._table_mapping()
                    # db_table = TablePeople()
                    db_table = table_mapping[label]
                    db_table.hashed_url = self._hashed_url
                    db_table.name = entity_name
                    self._session.add(db_table)

    def _table_mapping(self):
        """
        Returns a map with the api's label as a key and the class that can
        handle a request as a value
        """
        return { \
            ZmbLabels.Article.Entity.Movement.api(): TableMovements(),
            ZmbLabels.Article.Entity.People.api(): TablePeople(),
            ZmbLabels.Article.Entity.Educational.api(): TableEducationals(),
            ZmbLabels.Article.Entity.Private.api(): TablePrivates(),
            ZmbLabels.Article.Entity.Public.api(): TablePublics(),
            ZmbLabels.Article.Entity.Work.api(): TableWorks(),
            ZmbLabels.Article.Entity.City.api(): TableCities(),
            ZmbLabels.Article.Entity.State.api(): TableStates(),
            ZmbLabels.Article.Entity.Country.api(): TableCountries(),
            ZmbLabels.Article.Entity.Law.api(): TableLaws(),
            ZmbLabels.Article.Entity.Police.api(): TablePolices(),
            ZmbLabels.Article.Entity.Political.api(): TablePoliticals(),
            #ZmbLabels.Article.Entity.Action.api(): TableActions(),
        }

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
            for entity_ in ZmbLabels.Article.Entity.all_labels_n_metainfo():
                # if an entity_ is not in the output_map
                if (not entity_ in output_map[hash_].keys()):
                    # Creates an entry with an empty list in output_map
                    output_map[hash_][entity_] = []
        return output_map
