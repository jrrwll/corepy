"""
pip3 install cryptography
"""

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from corepy.conv.tunc import tunc_to_8_byte


def aes_encrypt(text, key, iv=None):
    if not iv:
        iv = tunc_to_8_byte(key)
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)

    encryptor = cipher.encryptor()
    return encryptor.update(text.encode()) + encryptor.finalize()


def aes_decrypt(text, key, iv=None):
    if not iv:
        iv = tunc_to_8_byte(key)
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)

    decryptor = cipher.decryptor()
    return decryptor.update(text.encode()) + decryptor.finalize()
