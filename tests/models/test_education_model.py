import pytest
from models.eductation_model import Education, EducationEntry


def test_education_model_success():
    data = {
        "entries": [
            {
                "institution": "University of Test",
                "degree": "Bachelor of Science in Testing",
                "field_of_study": "Software Testing",
                "start_year": "2018",
                "end_year": "2022",
                "gpa": 3.8,
            }
        ]
    }
    education = Education(**data)
    assert len(education.entries) == 1
    assert education.entries[0].institution == "University of Test"


def test_education_model_failure():
    data = {
        "entries": [
            {
                "institution": "University of Test",
                "degree": "Bachelor of Science in Testing",
                "field_of_study": "Software Testing",
                "start_year": "2018",
                "end_year": "2022",
                "gpa": 5.0,  # Invalid GPA
            }
        ]
    }
    with pytest.raises(ValueError):
        Education(**data)
