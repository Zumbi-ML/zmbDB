from db.tables.tb_definitions import TableUsers
from db.authorizer import create_api_key
from db.utils import get_session

def add_user(name, code, session=None, pl=0):
    key = create_api_key()
    user = TableUsers(name=name, code=code, api_key=key, perm_level=pl)
    if (not session):
        session = get_session()
    session.add(user)
    session.commit()
    session.close()
    return key
