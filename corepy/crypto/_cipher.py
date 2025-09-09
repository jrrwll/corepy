import base64
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# AES-128-CBC + HMAC-SHA256
class FernetCryptoProvider:

    def __init__(self, base64_key: str):
        key = base64.urlsafe_b64decode(base64_key)
        self.fernet = Fernet(key)

    @classmethod
    def generate_base64_key(cls) -> str:
        return base64.urlsafe_b64encode(Fernet.generate_key()).decode()

    def encrypt(self, plain: bytes) -> bytes:
        return self.fernet.encrypt(plain)

    def encrypt_as_str(self, plain: str) -> str:
        encrypted = self.encrypt(plain.encode())
        return base64.urlsafe_b64encode(encrypted).decode()

    def decrypt(self, cipher: bytes) -> bytes:
        return self.fernet.decrypt(cipher)

    def decrypt_as_str(self, encrypted: str) -> str:
        data = base64.urlsafe_b64decode(encrypted)
        decrypted = self.decrypt(data)
        return decrypted.decode()


class AesCryptoProvider:

    def __init__(self, base64_key: str, block_size: int):
        self.pkcs = padding.PKCS7(block_size)

        key = base64.urlsafe_b64decode(base64_key)
        self.key = self.padding(key)
        self.algorithm = algorithms.AES(self.key)

    def padding(self, plain: bytes) -> bytes:
        padder = self.pkcs.padder()
        return padder.update(plain) + padder.finalize()

    def unpadding(self, plain: bytes) -> bytes:
        unpadder = self.pkcs.unpadder()
        return unpadder.update(plain) + unpadder.finalize()

    @classmethod
    def from_aes128_cbc(cls, base64_key: str):
        return cls(base64_key, 128)

    @classmethod
    def from_aes192_cbc(cls, base64_key: str):
        return cls(base64_key, 192)

    @classmethod
    def from_aes256_cbc(cls, base64_key: str):
        return cls(base64_key, 256)

    @classmethod
    def from_aes512_cbc(cls, base64_key: str):
        return cls(base64_key, 512)

    def encrypt(self, plain: bytes) -> bytes:
        iv = os.urandom(16)
        encryptor = Cipher(
            self.algorithm, modes.CBC(iv)
        ).encryptor()

        padded = self.padding(plain)
        return iv + encryptor.update(padded) + encryptor.finalize()

    def encrypt_as_str(self, plain: str) -> str:
        encrypted = self.encrypt(plain.encode())
        return base64.urlsafe_b64encode(encrypted).decode()

    def decrypt(self, data: bytes) -> bytes:
        iv, data = data[:16], data[16:]

        decryptor = Cipher(
            self.algorithm, modes.CBC(iv)
        ).decryptor()

        plain = decryptor.update(data) + decryptor.finalize()
        return self.unpadding(plain)

    def decrypt_as_str(self, encrypted: str) -> str:
        data = base64.urlsafe_b64decode(encrypted)
        decrypted = self.decrypt(data)
        return decrypted.decode()
