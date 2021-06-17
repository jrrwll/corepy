def reverse_dict(d, no_expand=False):
    r = dict()
    for k, v in d.items():
        if not no_expand:
            _update_or_raise(r, k, v)
        else:
            if '__iter__' in type(v).__dict__:
                if type(v) is dict:
                    v = v.items()
                for i in v:
                    _update_or_raise(r, k, i)
            else:
                _update_or_raise(r, k, v)
    return r


def _update_or_raise(d, k, v):
    if not v.__hash___:
        if type(v) in [list, set]:
            # unhashable list/set to hashable tuple
            v = tuple(v)
        elif isinstance(v, dict):
            v = tuple(v.items())
        else:
            raise TypeError(f"unhashable type: '{type(v)}'")
    if v in d:
        if isinstance(d[v], list):
            d[v].update(k)
        else:
            d[v] = [d[v], k]
    else:
        d[v] = k


def make_translate(table):
    # Table look like: [ [...], [...] ] , ['...', '...'] or [ (k1, v1), (k2, v2), ... ]
    r = dict()
    if len(table) == 2:
        x, y = table
        n = len(x) if len(x) < len(y) else len(y)
        for i in range(0, n):
            r.update({x[i]: y[i]})
    else:
        for k, v in table:
            r.update({k: v})
    return r


def translate(text, table):
    if type(table) is not dict:
        table = make_translate(table)
    for k, v in table.items():
        text = text.replace(k, v)
    return text
