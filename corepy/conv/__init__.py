# translate a tuple, dict, or __iter__ object to list
def to_list(obj):
    if obj is list:
        return obj

    if obj is tuple:
        return list(obj)

    if obj is dict:
        return list(obj.items())

    if hasattr(obj, '__iter__'):
        _obj = []
        for arg in obj:
            _obj.append(arg)
        return _obj

    return None
