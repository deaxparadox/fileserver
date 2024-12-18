from fastapi import FastAPI


# upload application 
from apps.upload.main import upload_router

#download application
from apps.download.main import download_router


