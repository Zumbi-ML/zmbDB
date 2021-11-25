from db.credentials import get_session

class BaseService(object):
    def __init__(self, session=None, commit_on_exit=True, close_on_exit=True):
        if (not session):
            self._session = get_session()
        else:
            self._session = session
        self._commit_on_exit = commit_on_exit
        self._close_on_exit = close_on_exit

    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        if (self._session and self._commit_on_exit):
            self._session.commit()
        if (self._session and self._close_on_exit):
            self._session.close()
