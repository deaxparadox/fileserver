from fastapi import APIRouter, Response, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer

from apps.upload.helpers import generate_id
from apps.authentication import cruds, schema
from core.database import get_db


auth_router = APIRouter(
    prefix="/v1",
    tags=["auth", "authentication"],
)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@auth_router.get("/auth")
async def authentication_root(db: Session =  Depends(get_db)):
    users = await cruds.get_all_user(db)
    
    if isinstance(users, dict):
        return JSONResponse({}, status_code=status.HTTP_200_OK)

    if isinstance(users, list):
        return Response(
            {"users", users},
            status_code=status.HTTP_200_OK
        )
        
@auth_router.post("/create_user/")
async def create_user(user_schema: schema.UserRequestSchema):
    print(user_schema.model_dump())
    
    # password = generate_id(40)
    # user_schema = schema.UserRequestSchema(username=username, password=password, email=email)
    # new_user = await cruds.create_user(user_schema, session)
    # return Response({"user": new_user}, status_code=status.HTTP_201_CREATED)
    return {}


@auth_router.get("/users/me")
async def read_users_me(current_user: Annotated[schema.UserSchema, Depends(cruds.get_current_user)]):
    return current_user