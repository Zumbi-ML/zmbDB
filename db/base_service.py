from db.credentials import get_session

class BaseService(object):
    def __init__(self, commit_on_exit=True, close_on_exit=True):
        self._session = get_session()
        self._commit_on_exit = commit_on_exit
        self._close_on_exit = close_on_exit

    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        if (self._session and self._commit_on_exit):
            self._session.commit()
        if (self._session and self._close_on_exit):
            self._session.close()
