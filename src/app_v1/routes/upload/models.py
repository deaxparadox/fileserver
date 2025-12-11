from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from core.database import Base



class Upload(Base):
    __tablename__ = "upload"
    
    fid = Column(
        String(36), 
        primary_key=True,
        unique=True,
        comment="Code file storing the file."
    )
    filename = Column(
        String(256),
        comment="Name of uploaded file"
    )
