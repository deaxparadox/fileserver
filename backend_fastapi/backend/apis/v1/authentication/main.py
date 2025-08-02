from typing import Annotated

from fastapi import APIRouter, Response, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from ..v1 import router_auth_v1
from backend.apis.v1.upload.helpers import generate_id
from backend.apis.v1.authentication import cruds, schema
from backend.core.v1.database import get_db



auth_router = router_auth_v1

@auth_router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = cruds.fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(
            status_code=400,
            detail="Incorrect username and password."
        )
    user = cruds.UserInDBSchema(**user_dict)
    hashed_passwrod = cruds.fake_hash_password(form_data.password)
    if not hashed_passwrod == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username and password")
    return {"access_token": user.username, "token_type": "bearer"}


@auth_router.get("/auth/users/me")
async def read_users_me(
    current_user: Annotated[schema.UserSchema, Depends(cruds.get_current_user)]
):
    return current_user


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

