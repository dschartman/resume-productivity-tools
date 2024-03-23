from typing import List
from pydantic import BaseModel, Field
from models.core_info_model import CoreInfo
from models.eductation_model import Education
from models.experience_model import Job, Project
from models.skills_model import Skills


class ResumeInfo(BaseModel):
    """
    Aggregates all necessary information for a comprehensive resume.

    This model integrates personal and contact information, educational background,
    job experience, projects, and skills into a unified structure, facilitating
    easy generation and customization of resumes.

    Attributes:
        core_info (CoreInfo): Personal and contact information.
        education (Education): Educational background.
        jobs (List[Job]): List of job experiences.
        projects (List[Project]): List of projects worked on.
        skills (Skills): Set of skills and proficiencies.
    """

    core_info: CoreInfo = Field(..., description="Personal and contact information.")
    education: Education = Field(..., description="Educational background.")
    jobs: List[Job] = Field(..., description="List of job experiences.")
    projects: List[Project] = Field(..., description="List of projects worked on.")
    skills: Skills = Field(..., description="Set of skills and proficiencies.")
