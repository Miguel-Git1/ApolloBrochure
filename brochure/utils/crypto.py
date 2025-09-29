from typing import Union
from cryptography.fernet import Fernet

def generate_key() -> bytes:
    key: bytes = Fernet.generate_key()
    return key

def encrypt_data(literal: Union[bytes, str]) -> bytes:
    key = generate_key()
    encryptor = Fernet(key)

    return encryptor.encrypt(literal)



    