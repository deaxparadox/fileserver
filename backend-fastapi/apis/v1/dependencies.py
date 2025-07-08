from fastapi import Depends, File, UploadFile, Header, HTTPException, status
from sqlalchemy.orm import Session
from typing import Annotated

from core.database import get_db

class UploadDependency:
    def __init__(self,  db: Annotated[Session, Depends(get_db)], file: Annotated[UploadFile, File(description="Upload a file.")] = None):
        self.file = file
        self.db = db
    
    
def content_type_multipart_form_data(content_type: Annotated[str, Header()]):
    """
    Upload post request must be of type `multi-part/form-data`
    """
    # print(content_type, "multipart/form-data" in content_type)
    if "multipart/form-data" not in content_type:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST, 
            detail="Only accept multipart/form-data"
        )