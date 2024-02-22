from uuid import uuid4, UUID  
from datetime import datetime  
  
from sqlalchemy import text  
from sqlmodel import Field, SQLModel  
  
 
  
  
class TimestampModel(SQLModel):  
    created_at: datetime = Field(  
        default_factory=datetime.utcnow,  
        nullable=False,  
        sa_column_kwargs={"server_default": text("current_timestamp(0)")},  
    )