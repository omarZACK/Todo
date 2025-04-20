from base64 import b64encode, b64decode
from binascii import Error as BinasciiError

def encode_email(email):
    return b64encode(email.encode()).decode()

def decode_email(encoded_email):
    try:
        return b64decode(encoded_email.encode()).decode()
    except (BinasciiError, ValueError):
        return None
