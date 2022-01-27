from db.base_service import BaseService
from db.tb_searchers.searchers import *
from zmb_labels import ZmbLabels

class StatsService(BaseService):
    """
    This class offers indicators about the entities
    """

    def __init__(self, session=None):
        """
        Constructor
        """
        super().__init__(session=session)

    def count_entities(self):
        """
        Counts all the entities per entity type
        """

        result_map = {}

        with SourcesSearcher(self._session) as searcher:
            result_map[ZmbLabels.Article.Source.api()] = searcher.count()

        with MediaSearcher(self._session) as searcher:
            result_map[ZmbLabels.Article.Entity.Media.api()] = searcher.count()

        with MovementsSearcher(self._session) as searcher:
            result_map[ZmbLabels.Article.Entity.Movement.api()] = searcher.count()

        with PeopleSearcher(self._session) as searcher:
            result_map[ZmbLabels.Article.Entity.People.api()] = searcher.count()

        with EducationalSearcher(self._session) as searcher:
            result_map[ZmbLabels.Article.Entity.Educational.api()] = searcher.count()

        with PrivateSearcher(self._session) as searcher:
            result_map[ZmbLabels.Article.Entity.Private.api()] = searcher.count()

        with PublicSearcher(self._session) as searcher:
            result_map[ZmbLabels.Article.Entity.Public.api()] = searcher.count()

        with WorksSearcher(self._session) as searcher:
            result_map[ZmbLabels.Article.Entity.Work.api()] = searcher.count()

        with CitiesSearcher(self._session) as searcher:
            result_map[ZmbLabels.Article.Entity.City.api()] = searcher.count()

        with StatesSearcher(self._session) as searcher:
            result_map[ZmbLabels.Article.Entity.State.api()] = searcher.count()

        with CountriesSearcher(self._session) as searcher:
            result_map[ZmbLabels.Article.Entity.Country.api()] = searcher.count()

        with LawsSearcher(self._session) as searcher:
            result_map[ZmbLabels.Article.Entity.Law.api()] = searcher.count()

        with PolicesSearcher(self._session) as searcher:
            result_map[ZmbLabels.Article.Entity.Police.api()] = searcher.count()

        with PoliticalSearcher(self._session) as searcher:
            result_map[ZmbLabels.Article.Entity.Political.api()] = searcher.count()

        #with ActionsSearcher(self._session) as searcher:
        #    result_map[ACTIONS] = searcher.count()

        return result_map
