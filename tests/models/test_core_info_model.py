import pytest
from models.core_info_model import CoreInfo


def test_core_info_model_success():
    data = {
        "name": "John Doe",
        "address": "123 Main St",
        "email": "john@example.com",
        "phone": "123-456-7890",
        "linkedin": "https://linkedin.com/in/johndoe",
        "github": "https://github.com/johndoe",
    }
    core_info = CoreInfo(**data)
    assert core_info.name == data["name"]
    assert core_info.address == data["address"]


def test_core_info_model_failure():
    data = {
        "name": "John Doe",
        "address": "123 Main St",
        "email": "not-an-email",
        "phone": "123-456-7890",
    }
    with pytest.raises(ValueError):
        CoreInfo(**data)
