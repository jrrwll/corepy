import json
from urllib import parse

import requests

_request_methods = {
    "get": requests.get,
    "post": requests.post,
    "put": requests.put,
    "delete": requests.delete,
    "head": requests.head,
    "options": requests.options,
    "patch": requests.patch,
}


def request_get(url, params, headers):
    return request('get', url, params, headers)


def request_post(url, params, headers, data):
    return request('post', url, params, headers, data)


def request_put(url, params, headers, data):
    return request('put', url, params, headers, data)


def request_delete(url, params, headers, data):
    return request('delete', url, params, headers, data)


def request(method, url, params, headers, data=None):
    req = _request_methods.get(method, requests.post)
    if data is None:
        return req(url=url, params=params, headers=headers)

    headers = _lower_key_(headers)
    content_type = headers.get('content-type')
    # avoid headers has {'content-type': None}. if so, headers.get('content-type', '') still return None
    content_type = content_type.lower() if content_type else ''

    # x-www-form-urlencoded
    if content_type.startswith("application/x-www-form-urlencoded"):
        if type(data) is str:
            data = parse.quote(data)
        else:
            data = parse.urlencode(data)
    # json
    else:
        if type(data) is str:
            data = json.loads(data)

    return req(url=url, params=params, headers=headers, data=data)


def _lower_key_(old_dict):
    new_dict = {}
    for k, v in old_dict.items():
        # duck type
        if 'lower' in k.__dir__():
            new_dict[k.lower()] = v
        else:
            new_dict[k] = v
    return new_dict
