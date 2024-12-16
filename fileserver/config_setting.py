import os
from typing import Any




class GETENV:
    """
    Params:
    
    key: env variable
    type: conversion type, env will be converted to following type, varibles can only be converted into native types.
    
    """
    def __init__(self, key: str, default: Any | None = None, type: Any | None = None):
        self.__navtive_type = [int, float]
        self.key = key
        self.type = type
        self.default = default

    def _getenv(self) -> Any:
        env = os.getenv(self.key)
        
        if not env:
            if self.default:
                env = self.default
        else:
            if self.type:
                env = self.type(env)
            
        return env            
        
    def __call__(self):
        env = self._getenv()
        return env

    # def __gt__(self, )

# # configuration env
# WORKERS = GETENV('WORKERS', type=int)


# PORT = GETENV('PORT', type=int)

# "__all__" == ['WORKERS', 'PORT']