# -*- coding: UTF-8 -*-

import hashlib

def hash_url(url):
    encoded = url.encode('utf-8')
    return hashlib.md5(encoded).hexdigest()
