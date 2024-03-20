from typing import List
from pydantic import BaseModel, Field
from typing import Optional


class EducationEntry(BaseModel):
    institution: str = Field(..., example="University of Example")
    degree: str = Field(..., example="Bachelor of Science in Computer Science")
    field_of_study: str = Field(..., example="Computer Science")
    start_year: Optional[str] = Field(..., example="2018")
    end_year: str = Field(..., example="2022")
    gpa: Optional[float] = Field(None, ge=0.0, le=4.0, example=3.5)


class Education(BaseModel):
    entries: List[EducationEntry]
