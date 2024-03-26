from pydantic import BaseModel, DirectoryPath, FilePath
from typing import List


class ResumeConfig(BaseModel):
    core_info: FilePath
    education: FilePath
    jobs: DirectoryPath
    projects: List[DirectoryPath]
    skills: FilePath
    summary: FilePath
    template_name: str
