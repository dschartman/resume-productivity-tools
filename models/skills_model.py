from typing import List, Optional
from pydantic import BaseModel


class Skills(BaseModel):
    Programming_Languages: Optional[List[str]] = []
    Frameworks_and_Libraries: Optional[List[str]] = []
    Tools_and_Platforms: Optional[List[str]] = []
    Cloud_Platforms: Optional[List[str]] = []
    AI_ML: Optional[List[str]] = []
    Methodologies: Optional[List[str]] = []
    Databases: Optional[List[str]] = []
