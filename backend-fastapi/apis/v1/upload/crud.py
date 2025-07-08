from fastapi import Depends
from sqlalchemy.orm import Session
from apps.upload import helpers, schema, models

async def create_upload(filename: str, db: Session):
    fid = helpers.generate_id()
    db_upload = models.Upload(fid=fid, filename=filename)
    db.add(db_upload)
    db.commit()
    db.refresh(db_upload)
    return db_upload


async def get_all(db: Session):
    uploads = db.query(models.Upload).all()
    return uploads