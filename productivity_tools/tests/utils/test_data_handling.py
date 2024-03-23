import json
import pytest
from utils.data_handeling import load_json_data, validate_data
from models.core_info_model import CoreInfo


def test_load_json_data(tmpdir):
    sample_data = {
        "name": "Jane Doe",
        "address": "456 Elm St",
        "email": "jane@example.com",
        "phone": "987-654-3210",
    }
    file = tmpdir.join("sample.json")
    file.write(json.dumps(sample_data))
    loaded_data = load_json_data(file.strpath)

    assert loaded_data == sample_data


def test_validate_data_success():
    data = {
        "name": "Jane Doe",
        "address": "456 Elm St",
        "email": "jane@example.com",
        "phone": "987-654-3210",
    }
    validated_data = validate_data(data, CoreInfo)

    assert isinstance(validated_data, CoreInfo)


def test_validate_data_failure():
    data = {
        "name": "Jane Doe",
        "address": "456 Elm St",
        "email": "not-an-email",
        "phone": "987-654-3210",
    }
    with pytest.raises(ValueError):
        validate_data(data, CoreInfo)
