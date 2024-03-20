from typing import List, Optional
from pydantic import BaseModel, Field
from models.skills_model import Skills


class Role(BaseModel):
    title: str = Field(..., example="Senior Software Developer")
    responsibilities: List[str] = Field(
        ..., example=["Led development of Project Alpha"]
    )


class Job(BaseModel):
    id: str
    company: str
    location: str
    role: Role
    start_date: str
    end_date: Optional[str] = None
    projects: List[str] = []


class Project(BaseModel):
    id: str
    name: str
    description: str
    technologies_used: Skills
    achievements: List[str]
    job_id: str
    contributions: List[str]
