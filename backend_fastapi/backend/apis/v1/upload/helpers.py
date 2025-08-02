
import os
from binascii import hexlify

def generate_id(default_length=36) -> str:
    return hexlify(os.urandom(default_length)).decode('utf-8')