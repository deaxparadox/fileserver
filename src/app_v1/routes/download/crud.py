import os
from sqlalchemy.orm import Session

from apps.upload import models, helpers


async def search_file(fid: str, db: Session):
    db_query = db.query(models.Upload).get(fid)
    # filepath, filename = helpers.generate_filename(db_query.filename), db_query.filename
    return helpers.generate_filename(db_query.filename), db_query.filename