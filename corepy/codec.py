import hashlib
from pathlib import Path


def md5(s: str | bytes) -> str:
    if isinstance(s, str):
        s = s.encode("utf-8")
    return hashlib.md5(s).hexdigest()


def file_md5(file_path: str | Path) -> str:
    hash_md5 = hashlib.md5()

    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(8 << 20), b""):
            hash_md5.update(chunk)

    return hash_md5.hexdigest()


def sha256(s: str | bytes) -> str:
    if isinstance(s, str):
        s = s.encode("utf-8")
    return hashlib.sha256(s).hexdigest()
