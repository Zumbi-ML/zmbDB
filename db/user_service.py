from db.authorizer import Authorizer
from db.base_service import BaseService
from db.tables.tb_definitions import TableUsers
from db.credentials import get_session

class UserService(BaseService):

    def add_user(self, name, code):
        """
        Add a user to the session
        """
        key = Authorizer.create_api_key()
        user = TableUsers(name=name, code=code, api_key=key, perm_level=0)
        self._session.add(user)
        return key
