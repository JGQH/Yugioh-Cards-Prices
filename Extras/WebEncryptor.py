from cryptography.fernet import Fernet

KEY = b'32068Bzl1MLWkaCcUcgFvPgr4IOOGoVSd9qqk70vbko='

def encrypt_code(code:str)->str:
    global KEY
    encryptor = Fernet(KEY)

    bCode = code.encode()
    return encryptor.encrypt(bCode).decode()