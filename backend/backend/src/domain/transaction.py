from sqlmodel import SQLModel  
  
from .. import UUIDModel, TimestampModel  
  
  
class TransactionBase(SQLModel):  
    amount: int  
    description: str  
  
  
class Transaction(TransactionBase, UUIDModel, TimestampModel, table=True):  
    ...