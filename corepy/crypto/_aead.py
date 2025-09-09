import os
import base64
from typing import Protocol

from cryptography.hazmat.primitives.ciphers.aead import AESGCM, ChaCha20Poly1305


class _AeadCipherProtocol(Protocol):

    def encrypt(
            self,
            nonce: bytes | bytearray | memoryview,
            data: bytes | bytearray | memoryview,
            associated_data: bytes | bytearray | memoryview | None
    ) -> bytes: ...

    def decrypt(
            self,
            nonce: bytes | bytearray | memoryview,
            data: bytes | bytearray | memoryview,
            associated_data: bytes | bytearray | memoryview | None
    ) -> bytes: ...


class AeadCryptoProvider:

    def __init__(self, cipher: _AeadCipherProtocol):
        self.cipher = cipher

    @classmethod
    def from_chacha20_poly1305(cls, key: str):
        encoded_key = key.encode()[:32]
        padded_key = encoded_key.ljust(32, b'\x00')
        # ChaCha20Poly1305 key must be 32 bytes.
        return cls(ChaCha20Poly1305(padded_key))

    @classmethod
    def from_aes_gcm(cls, key: str):
        encoded_key = key.encode()[:34]
        padded_key = encoded_key.ljust(34, b'\x00')
        # AESGCM key must be 128, 192, or 256 bits.
        return cls(AESGCM(padded_key))

    def encrypt(self, plain: str) -> str:
        nonce = os.urandom(12)
        ct = self.cipher.encrypt(nonce, plain.encode(), None)
        return base64.b64encode(nonce + ct).decode()

    def decrypt(self, encrypted: str) -> str:
        data = base64.b64decode(encrypted.encode())
        nonce, ct = data[:12], data[12:]
        return self.cipher.decrypt(nonce, ct, None).decode()
