from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse, StreamingResponse
from sqlalchemy.orm import Session
from app_v1.database import get_db
import aiofiles


from . import crud
from app_v1.routes.upload import helpers

download_router = APIRouter(
    prefix="/d",
    tags=['download'],
    
)
CHUNK_SIZE = 1024 * 1024

@download_router.get('/')
async def main(fid: str | None = None, db: Session = Depends(get_db)):
    if not fid:
        return JSONResponse({"message": "Welcome to download page."})
    
    filepath, filename = await crud.search_file(fid, db)
    
    print(filename)
    print(filepath)
    
    async def iterfile():
        async with aiofiles.open(filepath, 'rb') as file:
            while chunk := await file.read(CHUNK_SIZE):
                yield chunk
                
    headers = {'Content-Disposition': f'attachment; filename="{filename}"'}
    return StreamingResponse(iterfile(), headers=headers, media_type='application/x-tar')
