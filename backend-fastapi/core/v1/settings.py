import os
from pathlib import Path
from . import helpers

BASE_DIR = Path(__file__).resolve().parent.parent.parent
PROJECT_DIR = BASE_DIR.parent
print("#############################", BASE_DIR)
print("#############################", PROJECT_DIR)

async def check_upload():
    global UPLOAD_DIR
    UPLOAD_DIR = await helpers.create_folder(BASE_DIR, "uploads")


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