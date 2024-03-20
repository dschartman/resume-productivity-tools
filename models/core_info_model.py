from pydantic import BaseModel, EmailStr, HttpUrl, StrictStr
from typing import Optional


class CoreInfo(BaseModel):
    name: StrictStr
    address: StrictStr
    email: EmailStr
    phone: str
    linkedin: Optional[HttpUrl] = None
    github: Optional[HttpUrl] = None
