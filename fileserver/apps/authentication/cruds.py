from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List, Annotated


from apps.authentication.schema import UserRequestSchema, UserSchema
from apps.authentication.models import UserModel
from apps.authentication.main import oauth2_scheme

async def get_all_user(db: Session) -> List[UserModel] | dict:
    users = db.query(UserModel).all()
    if len(users) == 0:
        return {}
    return users

async def create_user(user_schema: UserRequestSchema, session: Session):
    user = UserModel(user_schema.model_dump())
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def fake_decode_token(token: str) -> UserSchema:
    return UserSchema(
        username=token+'fakedecoded',
        email="deaxparadox@gmail.com",
        full_name="deaxparadox"
    )
    
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user