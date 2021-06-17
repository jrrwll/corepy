import base64


# return a str-like nor bytes-likes
def b64encode(data):
    return base64.standard_b64encode(data).decode()


def b64decode(data):
    return base64.standard_b64decode(data)


# The alphabet uses '-' instead of '+' and '_' instead of '/'.
def urlsafe_b64encode(data):
    return base64.urlsafe_b64encode(data)


def urlsafe_b64decode(data):
    return base64.urlsafe_b64decode(data)


'''
base64 32 16 85
'''


def base64_it(text, method=64):
    if method == 32:
        return base64.b32encode(text)
    elif method == 16:
        return base64.b16encode(text)
    elif method == 85:
        return base64.b85encode(text)
    else:
        return base64.b64encode(text)


def unbase64_it(text, method=64):
    if method == 32:
        return base64.b32decode(text)
    elif method == 16:
        return base64.b16decode(text)
    elif method == 85:
        return base64.b85decode(text)
    else:
        return base64.b64decode(text)

# ------------------------- bz2, gzip, zlib ----------------------------
