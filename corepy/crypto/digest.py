import hashlib


def md5str(text):
    md5 = hashlib.md5()
    if not isinstance(text, bytes):
        text = text.encode()
    md5.update(text)
    return md5.hexdigest()
