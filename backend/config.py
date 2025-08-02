import os
from typing import (
    Callable,
    Literal
)

from dotenv import load_dotenv


load_dotenv(override=True)


envrionment_list = Literal['local', 'prod', 'docker']
setting_file_list = Literal[
    "backend.settings.local",
    "backend.settings.prod"
]

class Config:
    ALLOWED_HOSTS: str = os.getenv("ALLOWED_HOSTS")
    DEBUG: str = os.getenv("DEBUG")
    ENVIRONMENT: envrionment_list = os.getenv("ENVIRONMENT")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    SETTING_FILE: setting_file_list = 'backend.settings.local'
    
    

    def __init__(self):
        _class_dict = self.__dir__()

        for k in _class_dict:
            if k.startswith("validate_"):
                func: Callable = getattr(self, k)
                func()

    def validate_debug(self):
        _check = bool(self.DEBUG)
        if not isinstance(_check, bool):
            raise RuntimeError("Invalid DEBUG value, need boolean")

    def validate_allowed_host(self):
        if not self.ALLOWED_HOSTS:
            raise RuntimeError("Invalid ALLOWED HOST")
        
        _ah = self.ALLOWED_HOSTS.split(",")
        if len(_ah) == 0 and not all([x == "" for x in _ah]):
            raise RuntimeError("Invalid ALLOWED HOST")
        
        if self.ALLOWED_HOSTS == '*':
            self.ALLOWED_HOSTS = [self.ALLOWED_HOSTS]
            
    def validate_environment(self):
        if self.ENVIRONMENT not in ['local', 'prod', 'docker']:
            raise RuntimeError("Incorrect environement") 
        
        if self.ENVIRONMENT == 'local':
            self.SETTING_FILE = "backend.settings.local"
        if self.ENVIRONMENT == 'prod':
            self.SETTING_FILE = "backend.settings.prod"

config = Config()

__all__ = ["config"]