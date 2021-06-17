import enum

import requests

# public import area
from .url import concat_url


# the core methods

@enum.unique
class HttpMethod(enum.Enum):
    GET = 0
    POST = 1
    PUT = 2
    DELETE = 3
    HEAD = 4
    PATCH = 5


class HttpRequest():
    def __init__(self):
        pass


class HttpClient():
    def __init__(self):
        pass


def request(url, method=HttpMethod.GET, body=None, headers=None, statement=None, **params):
    url = concat_url(url=url, statement=statement, **params)

    requests.get()
