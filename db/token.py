from random import randint
from constants import API_KEY_SIZE

QUOTE = 34
DOUBLE_QUOTE = 39

def create_api_key(n=API_KEY_SIZE):
    ini, end = 33, 126
    key = ""
    key_size = 0
    while (key_size < n):
        num = randint(ini, end + 1)
        if (num == QUOTE or num == DOUBLE_QUOTE):
            continue
        key += chr(num)
        key_size += 1
    return key
