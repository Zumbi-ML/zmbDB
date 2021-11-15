from db.credentials import get_session
from db.entities import entities_map
from db.tables.tb_definitions import *
from utils import str2date

class ArticleService(object):
    def __init__(self, article, entities):
        """
        Constructor
        """
        self._article = article
        self._entities = entities
        self._session = get_session()
        self._hashed_uri = None

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

    def __enter__(self):
        """
        Return the instance
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Commit and close the session
        """
        self._session.commit()
        self._session.close()
