def concat_url(url, statement=None, **params):
    if statement:
        statement = "#%s" % statement
    else:
        statement = ""

    if params:
        return url + '?' + '&'.join(["%s=%s" % (k, v) for k, v in params]) + statement
    else:
        return url + statement
