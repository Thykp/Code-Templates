from typing import Optional
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: EmailStr
