"""
pip3 install pycrypto
"""

from Crypto.Cipher import DES

from . import prepare_key_and_iv

BS = DES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-s[-1]]


def des_encrypt(data, key, iv=None):
    if not isinstance(data, str):
        data = data.decode()
    key, iv = prepare_key_and_iv(key, iv)

    des = DES.new(key, DES.MODE_CBC, bytes(iv))
    return des.encrypt(pad(data))


def des_decrypt(data, key, iv=None):
    key, iv = prepare_key_and_iv(key, iv)

    des = DES.new(key, DES.MODE_CBC, bytes(iv))
    return unpad(des.decrypt(data))
