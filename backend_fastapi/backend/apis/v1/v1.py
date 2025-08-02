from fastapi import APIRouter

router_auth_v1 = APIRouter(prefix="/auth")
router_download_v1 = APIRouter(prefix="/download")
router_upload_v1 = APIRouter(prefix="/upload")