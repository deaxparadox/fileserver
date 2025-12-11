import os
from pathlib import Path
import sys


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app_v1.routes import router_v1

# setting
from app_v1.database import SessionLocal, engine

from common import (
    config,
    logging
)


app = FastAPI()

app.include_router(router_v1, prefix="/api")


app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=config.ALLOWED_METHODS,
    allow_headers=config.ALLOWED_HEADERS
)

@app.get("/")
async def root():
    return {"message": "Welcome to download file server."}
