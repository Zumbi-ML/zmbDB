from constants import API_KEY_SIZE
from db.credentials import get_session
from db.tables.tb_definitions import TableUsers
from random import randint

class Authorizer(object):
    """
    Handles authorization issues in the database
    """

    def __init__(self):
        """
        Constructor
        """
        self._session = get_session()

    def __enter__(self):
        """
        On enter actions
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        On exit actions
        """
        self._session.close()

    def create_api_key(n=API_KEY_SIZE):
        """
        Creates an API key_size
        Args:
            n: API key size. Defaults to constants.API_KEY_SIZE
        """
        QUOTE, DOUBLE_QUOTE, APOSTROPHE = 34, 39, 96
        exceptions = [QUOTE, DOUBLE_QUOTE, APOSTROPHE]

        ini, end = 33, 126 # ASCII Codes
        key = ""
        key_size = 0
        while (key_size < n):
            num = randint(ini, end + 1)
            if (num in exceptions):
                continue
            key += chr(num)
            key_size += 1
        return key

    def is_api_key_valid(self, api_key):
        """
        Checks whether an API key is valid
        Args:
            api_key: the API key to be validated
        """
        is_valid = False
        result = self._session.query(TableUsers)                            \
                                    .filter(TableUsers.api_key == api_key)  \
                                        .scalar()
        is_valid = not result == None and result.api_key == api_key
        return is_valid
