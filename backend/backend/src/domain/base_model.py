from datetime import datetime

from sqlmodel import Column, DateTime, Field, SQLModel, func


class BaseModel(SQLModel):
    id: int = Field(primary_key=True)
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=func.now()))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=func.now(), onupdate=func.now()))
  
class UUIDModel(SQLModel):  
    id: UUID = Field(  
        default_factory=uuid4,  
        primary_key=True,  
        index=True,  
        nullable=False,  
    ) 