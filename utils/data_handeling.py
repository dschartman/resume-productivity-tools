import json
from pydantic import ValidationError, BaseModel

from typing import Type, Dict, Any

import os
from typing import Type, List
from pydantic import BaseModel


def load_json_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def validate_data(data: Dict[str, Any], model: Type[BaseModel]) -> BaseModel:
    try:
        return model(**data)
    except ValidationError as e:
        print(f"Validation Error in {model.__name__}: {e.json()}")
        raise


def load_model(file_path, model: Type[BaseModel]) -> BaseModel:
    data = load_json_data(file_path)
    validated_data = validate_data(data, model)

    return validated_data


def load_models(path: str, model: Type[BaseModel]) -> List[BaseModel]:
    validated_models = []

    if not os.path.isdir(path):
        raise ValueError(f"The path {path} is not a directory.")

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        if not os.path.isfile(file_path):
            continue

        if filename.endswith(".json"):
            try:
                validated_model = load_model(file_path, model)
                validated_models.append(validated_model)
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")

    return validated_models
