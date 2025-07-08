
import os
from binascii import hexlify

from core import settings

def generate_id(default_length=36) -> str:
    return hexlify(os.urandom(default_length)).decode('utf-8')

def generate_filename(file: str) -> str:
    return os.path.join(settings.UPLOAD_DIR, file)