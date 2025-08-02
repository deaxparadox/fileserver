from typing import List, Annotated

from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session


from apps.authentication.schema import UserRequestSchema, UserSchema, UserInDBSchema
from apps.authentication.models import UserModel



fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}


def fake_hash_password(password: str):
    return "fakehashed" + password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def fake_decode_token(token: str) -> UserSchema:
    return UserSchema(
        username=token+'fakedecoded',
        email="deaxparadox@gmail.com",
        full_name="deaxparadox"
    )
    
def get_user(db, username: str):
    if username is db:
        user_dict = db[username]
        return UserInDBSchema(**user_dict)

def fake_decode_token(token):
    # 
    user = get_user(fake_users_db, token)
    return user
    
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return user


async def get_current_active_user(
    current_user: Annotated[UserSchema, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user



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

