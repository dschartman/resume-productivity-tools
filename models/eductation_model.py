from typing import List
from pydantic import BaseModel, Field
from typing import Optional


class EducationEntry(BaseModel):
    """
    An entry representing an individual's educational experience.

    Attributes:
        institution (str): Name of the educational institution.
        degree (str): Name of the degree earned.
        field_of_study (str): Field or major of study.
        start_year (Optional[str]): The start year of the education period.
        end_year (str): The end year or expected end year of the education period.
        gpa (Optional[float]): The Grade Point Average achieved, on a scale from 0.0 to 4.0.
    """

    institution: str = Field(..., example="University of Example")
    degree: str = Field(..., example="Bachelor of Science in Computer Science")
    field_of_study: str = Field(..., example="Computer Science")
    start_year: Optional[str] = Field(..., example="2018")
    end_year: str = Field(..., example="2022")
    gpa: Optional[float] = Field(None, ge=0.0, le=4.0, example=3.5)


class Education(BaseModel):
    """
    A collection of `EducationEntry` items representing the educational background of an individual.

    Attributes:
        entries (List[EducationEntry]): A list of education entries.
    """

    entries: List[EducationEntry]
