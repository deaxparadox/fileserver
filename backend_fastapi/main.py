import os
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.apis.v1.upload.main import upload_router
from backend.apis.v1.download.main import download_router
from backend.apis.v1.authentication.main import auth_router

# setting
from backend.core.v1.database import SessionLocal, engine

from backend.common import (
    config,
    logging
)


app = FastAPI()

app.include_router(upload_router)
app.include_router(download_router)
app.include_router(auth_router)


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
