from corepy.conv.tunc import tunc_to_8_byte


def prepare_key_and_iv(key, iv):
    # iv = bytearray([1,2,3,4,5,6,7,8])
    key = tunc_to_8_byte(key)
    if not iv:
        iv = key
    elif len(iv) != 8:
        iv = tunc_to_8_byte(iv)
    return key, iv
