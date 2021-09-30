def _makeIv(data):
    if not isinstance(data, bytes):
        data = data.encode()
    if len(data) < 8:
        data = data + b'\0' * (8 - len(data))
    return data[:8]
