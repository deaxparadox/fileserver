from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware



# upload application
from .apis.v1.upload.main import upload_router
from .apis.v1.download.main import download_router
from .apis.v1.authentication.main import auth_router

# setting
from .core.v1 import settings


# database
from .core.v1.database import SessionLocal, engine

# models.Base.metadata.create_all(bind=engine)





app = FastAPI()

app.include_router(upload_router)
app.include_router(download_router)
app.include_router(auth_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=settings.ALLOWED_METHODS,
    allow_headers=settings.ALLOWED_HEADERS
)

@app.get("/")
async def root():
    return {"message": "Welcome to download file server."}
