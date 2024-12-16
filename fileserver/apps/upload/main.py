from typing import Annotated
import os
from fastapi import APIRouter, File, UploadFile, Depends
from fastapi.responses import Response, JSONResponse
from fastapi import status
from sqlalchemy.orm import Session
import aiofiles

from core.database import get_db
from core import settings
from apps.upload import crud, schema, helpers
from apps.dependencies import UploadDependency, content_type_multipart_form_data

upload_router = APIRouter(
    prefix="/v1",
    tags=['upload'],
)


# 
# get /v1/u/ returns the list of all uploaded files.
# 
@upload_router.get(
    "/u/",
    response_model=schema.ResponseListUploadModel
)
async def upload_message(
    dep = Depends(UploadDependency)
):
    uploads = await crud.get_all(db=dep.db)
    # return {"message": "upload here, using post method"}
    return {
        "uploaded": uploads
    }


# 
# post /v1/u/ -> upload a file.
# 
@upload_router.post(
    "/u/", 
    response_model=schema.ResponseUploadModel,
    status_code=status.HTTP_202_ACCEPTED,
)
async def upload_file(
    file: Annotated[UploadFile, File(description="Upload a file.")] = None, 
    db: Session =  Depends(get_db),
    check_content_type = Depends(content_type_multipart_form_data)
):
    
    # If no file uploaded
    if not file:
        return JSONResponse({
            "message": "No file uploaded"
        }, status_code=status.HTTP_400_BAD_REQUEST)

    filename = helpers.generate_filename(file.filename)
    
    
    uploadsize = 64 * 1024
    # filesize = file.size
    # block = filesize // uploadsize

    try:
        total_length = 0
        async with aiofiles.open(filename, 'wb') as uf:
            while content := await file.read(uploadsize):
                total_length+=len(content)
                await uf.write(content)

        # after successful upload
        # generate database `fid`
        db_upload = await crud.create_upload(filename=file.filename, db=db)
    
    except Exception as e:
        # if any exception occurs, during upload
        # return error message, with code `500`
        return {
            JSONResponse({
                "message": "There was an error uploading the file."
            }, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        }
    finally:
        await file.close()
        
    return db_upload



# 
# POST /v1/u/m/ -> Upload multiple files.
# 
@upload_router.post(
    "/u/m/", 
    response_model=schema.ResponseListUploadModel,
    status_code=status.HTTP_202_ACCEPTED
)
async def upload_multiple_file(
    files: Annotated[list[UploadFile], File(description="Multiple files uploads")], 
    db: Session =  Depends(get_db)
):
    
    # If no file uploaded
    if not files:
        return JSONResponse({
            "message": "No file uploaded"
        }, status_code=status.HTTP_400_BAD_REQUEST)

    
    uploadsize = 64 * 1024
    # filesize = file.size
    # block = filesize // uploadsize



    uploaded_files = []
    for file in files:
        try:    
            print(file.filename)
            filename = helpers.generate_filename(file.filename)
            total_length = 0
            async with aiofiles.open(filename, 'wb') as uf:
                while content := await file.read(uploadsize):
                    total_length+=len(content)
                    await uf.write(content)

            # after successful upload
            # generate database `fid`
            db_upload = await crud.create_upload(filename=file.filename, db=db)
            uploaded_files.append(db_upload)
            
        except Exception as e:
            # if any exception occurs, during upload
            # return error message, with code `500`
            return {
                JSONResponse({
                    "message": "There was an error uploading the file."
                }, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
            }
        finally:
            await file.close()
            
    return {
        "uploaded": uploaded_files
    }
    
    
# @upload_router.delete("/u/")
# def delete_upload_file():
#     return {}