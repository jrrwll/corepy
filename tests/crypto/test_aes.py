import base64

from corepy.crypto import AesCryptoProvider, FernetCryptoProvider


def test_aes():
    print("\nAesCryptoProvider")
    base64_key = base64.urlsafe_b64encode(b'abc').decode()
    print(base64_key)
    cipher = AesCryptoProvider.from_aes128_cbc(base64_key)
    encrypted = cipher.encrypt_as_str("Hello World!")
    print(encrypted)
    decrypted = cipher.decrypt_as_str(encrypted)
    print(decrypted)

    print("\nFernetCryptoProvider")
    base64_key = FernetCryptoProvider.generate_base64_key()
    print(base64_key)
    fernet = FernetCryptoProvider(base64_key)
    encrypted = fernet.encrypt_as_str("Hello World!")
    print(encrypted)
    decrypted = fernet.decrypt_as_str(encrypted)
    print(decrypted)
