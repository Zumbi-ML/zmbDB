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

    def count_entities(self, criteria):
        """
        Counts the ocurrences of the entities that satisfies the criteria
        """
        result_map = {}

        searchers = self._searcher_mapping()
        for key in criteria.keys():
            if (not criteria[key]):
                continue
            name = criteria[key]
            result_map[key] = searchers[key].count_by_name(name)

        return result_map

    def count_ents_by_freq(self, topk=10):
        """
        Counts the ocurrences of the entities
        """
        result_map = {}

        searchers = self._searcher_mapping()
        for key in searchers.keys():
            result_map[key] = searchers[key].count_by_freq(topk)

        return result_map

    def _searcher_mapping(self):
        """
        Returns a map with the api's label as a key and the class that can
        handle a request as a value
        """
        return { \
            ZmbLabels.Article.Entity.Movement.api(): MovementsSearcher(self._session),
            ZmbLabels.Article.Entity.People.api(): PeopleSearcher(self._session),
            ZmbLabels.Article.Entity.Educational.api(): EducationalSearcher(self._session),
            ZmbLabels.Article.Entity.Private.api(): PrivateSearcher(self._session),
            ZmbLabels.Article.Entity.Public.api(): PublicSearcher(self._session),
            ZmbLabels.Article.Entity.Work.api(): WorksSearcher(self._session),
            ZmbLabels.Article.Entity.City.api(): CitiesSearcher(self._session),
            ZmbLabels.Article.Entity.State.api(): StatesSearcher(self._session),
            ZmbLabels.Article.Entity.Country.api(): CountriesSearcher(self._session),
            ZmbLabels.Article.Entity.Law.api(): LawsSearcher(self._session),
            ZmbLabels.Article.Entity.Police.api(): PolicesSearcher(self._session),
            ZmbLabels.Article.Entity.Political.api(): PoliticalSearcher(self._session),
            ZmbLabels.Article.Entity.Media.api(): MediaSearcher(self._session),
            ZmbLabels.Article.Source.api(): SourcesSearcher(self._session),
            #ZmbLabels.Article.Entity.Action.api(): ActionsSearcher(self._session),
        }
