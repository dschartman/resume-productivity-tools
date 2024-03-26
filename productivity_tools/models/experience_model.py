from typing import List, Optional
from pydantic import BaseModel, Field
from models.skills_model import Skills  # Assuming this import path is correct


class Summary(BaseModel):
    content: str


class Role(BaseModel):
    """
    Represents the specific role held within a job, including title and responsibilities.

    Attributes:
        title (str): The job title or position.
        responsibilities (List[str]): A list of key responsibilities and duties.
    """

    title: str = Field(
        ...,
        example="Senior Software Developer",
        description="The job title or position.",
    )
    responsibilities: List[str] = Field(
        ...,
        example=[
            "Develop new user-facing features",
            "Ensure the technical feasibility of UI/UX designs",
        ],
        description="A list of key responsibilities and duties.",
    )


class Job(BaseModel):
    """
    Detailed information about a job or employment position, including the company, role, and duration.

    Attributes:
        id (str): A unique identifier for the job entry.
        company (str): The name of the company where the employment was held.
        location (str): The geographical location of the job.
        role (Role): A detailed description of the role held at the job.
        start_date (str): The start date of the employment, formatted as YYYY-MM-DD.
        end_date (Optional[str]): The end date of the employment, formatted as YYYY-MM-DD, or None for current positions.
        projects (List[str]): A list of identifiers for projects contributed to during this employment.
    """

    id: str = Field(..., description="A unique identifier for the job entry.")
    company: str = Field(
        ...,
        example="Tech Innovations Inc.",
        description="The name of the company where the employment was held.",
    )
    location: str = Field(
        ..., example="Tech City", description="The geographical location of the job."
    )
    role: Role = Field(
        ..., description="A detailed description of the role held at the job."
    )
    start_date: str = Field(
        ...,
        example="01-23",
        description="The start date of the employment, formatted as MM-YY.",
    )
    end_date: Optional[str] = Field(
        None,
        example="01-24",
        description="The end date of the employment, formatted as MM-YY.",
    )
    projects: List[str] = Field(
        default=[],
        description="A list of identifiers for projects contributed to during this employment.",
    )


class Project(BaseModel):
    """
    A project undertaken as part of a job, detailing the work done and technologies used.

    Attributes:
        id (str): A unique identifier for the project.
        name (str): The name of the project.
        description (str): A brief overview of the project's goals and outcomes.
        technologies_used (Skills): The skills and technologies utilized in the project.
        achievements (List[str]): Significant outcomes or successes achieved through the project.
        job_id (str): The ID of the job this project is associated with.
        contributions (List[str]): Specific contributions made towards the project.
    """

    id: str = Field(..., description="A unique identifier for the project.")
    name: str = Field(
        ...,
        example="Automation Suite Expansion",
        description="The name of the project.",
    )
    description: str = Field(
        ...,
        example="Expanded the automation suite by 50%.",
        description="A brief overview of the project.",
    )
    technologies_used: Skills = Field(
        ..., description="The skills and technologies utilized in the project."
    )
    achievements: List[str] = Field(
        ...,
        example=["Increased coverage by 50%", "Reduced execution time by 20%"],
        description="Significant outcomes or successes achieved.",
    )
    job_id: str = Field(
        ..., description="The ID of the job this project is associated with."
    )
    contributions: List[str] = Field(
        ...,
        example=["Developed new test cases", "Optimized test execution"],
        description="Specific contributions made towards the project.",
    )
