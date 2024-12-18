from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import mapped_column, Mapped

from core.database import Base


class PasswordModel(Base):
    __tablename__ = "password"
    
    sr_no = Column(Integer(), autoincrement=True, default=0)
    
    id = Column(
        String(36),
        comment="Password",
        primary_key=True,
        unique=True
    )
    
    password = Column(
        String(40),
        comment="Password table column"
    )
    
    __abstract__ = True


class UserModel(PasswordModel):
    __tablename__ = "user"

    
    def __repr__(self):
        return f"{self.__class__.__name__} ({self.username})"
    

    
    # 
    username = Column(
        String(24),
        unique=True,
        comment=("Username of user.")
    )
    first_name = Column(
        String(24),
        comment=("Firstname of the user"),
        nullable=True,
        
    )
    last_name = Column(
        String(24),
        comment=("Lastname of the user"),
        nullable=True
    )
    
    
    email = Column(
        String(56),
        comment=("Email of the user.")
    )

    
    
    # 
    is_active = Boolean(False)
    is_superuser = Boolean(False)