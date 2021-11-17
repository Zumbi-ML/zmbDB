from db.base_service import BaseService
from db.e_map import *
from db.tb_searchers.searchers import *

class EntityService(BaseService):
    def summary(self):
        result_map = {}
        with SourcesSearcher(self._session) as searcher:
            result_map[SOURCES] = searcher.summarize()

        with MediaSearcher(self._session) as searcher:
            result_map[MEDIA] = searcher.summarize()

        with MovementsSearcher(self._session) as searcher:
            result_map[MOVEMENTS] = searcher.summarize()

        with PeopleSearcher(self._session) as searcher:
            result_map[PEOPLE] = searcher.summarize()

        with EducationalSearcher(self._session) as searcher:
            result_map[EDUCATIONAL] = searcher.summarize()

        with PrivateSearcher(self._session) as searcher:
            result_map[PRIVATE] = searcher.summarize()

        with PublicSearcher(self._session) as searcher:
            result_map[PUBLIC] = searcher.summarize()

        with ActionsSearcher(self._session) as searcher:
            result_map[ACTIONS] = searcher.summarize()

        with WorksSearcher(self._session) as searcher:
            result_map[WORKS] = searcher.summarize()

        with CitiesSearcher(self._session) as searcher:
            result_map[CITIES] = searcher.summarize()

        with StatesSearcher(self._session) as searcher:
            result_map[STATES] = searcher.summarize()

        with CountriesSearcher(self._session) as searcher:
            result_map[COUNTRIES] = searcher.summarize()

        with LawsSearcher(self._session) as searcher:
            result_map[LAWS] = searcher.summarize()

        with PolicesSearcher(self._session) as searcher:
            result_map[POLICES] = searcher.summarize()
        return result_map
