from db.authorizer import Authorizer
from db.tables.tb_definitions import TableUsers
from db.credentials import get_session

class UserService(object):

    def __init__(self):
        """
        Constructor
        """
        self._session = get_session()

    def __enter__(self):
        """
        On object enter
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        On object exit
        """
        self._session.commit()
        self._session.close()

    def add_user(self, name, code):
        """
        Add a user to the session
        """
        key = Authorizer.create_api_key()
        user = TableUsers(name=name, code=code, api_key=key, perm_level=0)
        self._session.add(user)
        return key
