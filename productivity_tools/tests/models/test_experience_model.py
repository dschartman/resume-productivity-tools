import pytest
from models.experience_model import Job, Role
from models.experience_model import Project
from models.skills_model import Skills


def test_job_model_success():
    data = {
        "id": "job_1",
        "company": "Tech Innovations Inc.",
        "location": "Tech City",
        "role": {
            "title": "Lead Quality Assurance Engineer",
            "responsibilities": [
                "Develop test strategies",
                "Implement automation frameworks",
            ],
        },
        "start_date": "2020-01-01",
        "end_date": "2022-12-31",
        "projects": ["project_alpha", "project_beta"],
    }
    job = Job(**data)
    assert job.company == "Tech Innovations Inc."
    assert isinstance(job.role, Role)


def test_job_model_failure():
    data = {
        # Omitting required 'id' field
        "company": "Tech Innovations Inc.",
        "location": "Tech City",
        "start_date": "2020-01-01",
    }
    with pytest.raises(ValueError):
        Job(**data)


def test_project_model_success():
    """Test successful validation of the Project model."""
    data = {
        "id": "project_1",
        "name": "Automation Suite Expansion",
        "description": "Expanded the automation suite by 50%.",
        "technologies_used": Skills(Programming_Languages=["Python", "Java"]),
        "achievements": ["Increased coverage by 50%", "Reduced execution time by 20%"],
        "job_id": "job_1",
        "contributions": ["Developed new test cases", "Optimized test execution"],
    }
    project = Project(**data)
    assert project.name == "Automation Suite Expansion"
    assert "Python" in project.technologies_used.Programming_Languages


def test_project_model_failure():
    """Test validation failure with incorrect data type for 'technologies_used'."""
    data = {
        "id": "project_1",
        "name": "Automation Suite Expansion",
        "description": "Expanded the automation suite by 50%.",
        "technologies_used": ["Python", "Java"],  # Incorrect type
        "achievements": ["Increased coverage by 50%", "Reduced execution time by 20%"],
        "job_id": "job_1",
        "contributions": ["Developed new test cases", "Optimized test execution"],
    }
    with pytest.raises(ValueError):
        Project(**data)
