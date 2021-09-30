import base64
import random
import string
from unittest import TestCase


class TestDes(TestCase):
    key = ''.join(random.choice(string.ascii_letters) for _ in range(25))
    data = ''.join(random.choice(string.ascii_letters) for _ in range(76))
    print(f"data:\t{data}")
    print(f"key:\t{key}\n\n")

    def test_des(self):
        from corepy.crypto.des import des_encrypt, des_decrypt
        # input str
        encrypted_data = des_encrypt(self.data, self.key)
        print(f"encrypted_data:\t{base64.b64encode(encrypted_data).decode()}")
        # input bytes
        decrypted_data = des_decrypt(encrypted_data, self.key)
        print(f"decrypted_data:\t{decrypted_data.decode()}")

        from corepy.crypto.des import des_encrypt, des_decrypt
        # input bytes
        encrypted_data = des_encrypt(self.data.encode(), self.key)
        print(f"encrypted_data:\t{base64.b64encode(encrypted_data).decode()}")
        # input str
        decrypted_data = des_decrypt(encrypted_data, self.key)
        print(f"decrypted_data:\t{decrypted_data.decode()}")
