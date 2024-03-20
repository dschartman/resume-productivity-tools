from typing import List
from pydantic import BaseModel


class Skills(BaseModel):
    Programming_Languages: List[str]
    Frameworks_and_Libraries: List[str]
    Tools_and_Platforms: List[str]
    Cloud_Platforms: List[str]
    AI_ML: List[str]
    Methodologies: List[str]
    Databases: List[str]
