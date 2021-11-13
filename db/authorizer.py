from constants import API_KEY_SIZE
from db.tables.tb_definitions import TableUsers
from db.utils import get_session
from random import randint

QUOTE = 34
DOUBLE_QUOTE = 39
APOSTROPHE = 96

def create_api_key(n=API_KEY_SIZE):
    ini, end = 33, 126
    key = ""
    key_size = 0
    while (key_size < n):
        num = randint(ini, end + 1)
        if (num == QUOTE or num == DOUBLE_QUOTE or num == APOSTROPHE):
            continue
        key += chr(num)
        key_size += 1
    return key

def is_api_key_valid(api_key, session=None):
    is_valid = False
    if (not session):
        session = get_session()
    result = session.query(TableUsers).filter(TableUsers.api_key == api_key).scalar()
    is_valid = not result == None and result.api_key == api_key
    return is_valid
