from random import randint

def create(n):
    ini, end = 33, 126
    token = ""
    token_size = 0
    while (token_size < n):
        num = randint(ini, end + 1)
        if (num == 34 or num == 39):
            continue
        token += chr(num)
        token_size += 1
    return token
