from db.base_service import BaseService
from db.e_map import *
from db.tb_searchers.searchers import *

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
            result_map[SOURCES] = searcher.count()

        with MediaSearcher(self._session) as searcher:
            result_map[MEDIA] = searcher.count()

        with MovementsSearcher(self._session) as searcher:
            result_map[MOVEMENTS] = searcher.count()

        with PeopleSearcher(self._session) as searcher:
            result_map[PEOPLE] = searcher.count()

        with EducationalSearcher(self._session) as searcher:
            result_map[EDUCATIONAL] = searcher.count()

        with PrivateSearcher(self._session) as searcher:
            result_map[PRIVATE] = searcher.count()

        with PublicSearcher(self._session) as searcher:
            result_map[PUBLIC] = searcher.count()

        with ActionsSearcher(self._session) as searcher:
            result_map[ACTIONS] = searcher.count()

        with WorksSearcher(self._session) as searcher:
            result_map[WORKS] = searcher.count()

        with CitiesSearcher(self._session) as searcher:
            result_map[CITIES] = searcher.count()

        with StatesSearcher(self._session) as searcher:
            result_map[STATES] = searcher.count()

        with CountriesSearcher(self._session) as searcher:
            result_map[COUNTRIES] = searcher.count()

        with LawsSearcher(self._session) as searcher:
            result_map[LAWS] = searcher.count()

        with PolicesSearcher(self._session) as searcher:
            result_map[POLICES] = searcher.count()

        return result_map
