"""
pip3 install pyDes
"""

from pyDes import des, CBC, PAD_PKCS5

from . import prepare_key_and_iv


def des_encrypt(data, key, iv=None):
    key, iv = prepare_key_and_iv(key, iv)

    baseDes = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    return baseDes.encrypt(data, padmode=PAD_PKCS5)


def des_decrypt(data, key, iv=None):
    key, iv = prepare_key_and_iv(key, iv)

    baseDes = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    return baseDes.decrypt(data, padmode=PAD_PKCS5)
