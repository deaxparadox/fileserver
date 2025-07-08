from pydantic import BaseModel

class ResponseUploadModel(BaseModel):
    fid: str
    filename: str
    
class ResponseListUploadModel(BaseModel):
    uploaded: list[ResponseUploadModel]