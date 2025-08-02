from math import log
import os
from pathlib import Path
import sys
from typing import (
    Callable, 
    Optional
)


BASE_DIR = Path(__file__).resolve().parent.parent.parent
PROJECT_ROOT = BASE_DIR.parent

sys.path.append(BASE_DIR)


class Config:
    ALLOWED_HEADERS = [
        "text/json",
        "application/json",
        'multipart/form-data',
        "text/plain",
    ]
    ALLOWED_METHODS = [
        "GET",
        "OPTIONS"
        "POST",
    ]
    ALLOWED_ORIGINS = [
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "http://localhost:9000",
        "http://127.0.0.1:9000",
        "http://localhost:4200",
        "http://127.0.0.1:4200"
    ]
    BASE_DIR = BASE_DIR
    LOG_DIR = BASE_DIR / 'logs'
    PROJECT_ROOT = PROJECT_ROOT
    UPLOAD_DIR = BASE_DIR.joinpath("uploads")
    
    def __init__(self) -> None:
        keys = self.__dir__()
        
        for k in keys:
            if k.startswith("validate_"):
                f: Optional[Callable] = getattr(self, k, None)
                if not f:
                    raise RuntimeError("Unable validation the config: {}".format(k.split("_", 1)))
                f()
        
    def validate_log_dir(self):
        log_dir = Path(self.LOG_DIR)
        if not log_dir.exists():
            log_dir.mkdir(exist_ok=True)
        
    def validate_upload_dir(self):
        upload_dir = Path(self.UPLOAD_DIR)
        if not Path(self.LOG_DIR).exists():
            upload_dir.mkdir(exist_ok=True)
        
    
config = Config()


__all__ = [
    "config"
]