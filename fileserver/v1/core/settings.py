import os
from pathlib import Path
from . import helpers

BASE_DIR = Path("__file__").resolve().parent


UPLOAD_DIR = helpers.create_folder(BASE_DIR, "uploads")


ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:9000",
    "http://127.0.0.1:9000",
    "http://localhost:4200",
    "http://127.0.0.1:4200"
]


ALLOWED_METHODS = [
    "GET",
    "POST",
    "OPTIONS"
]

ALLOWED_HEADERS = [
    "text/json",
    "application/json",
    'multipart/form-data',
    "text/plain",
]