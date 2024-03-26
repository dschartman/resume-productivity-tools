import json
from pydantic import ValidationError, BaseModel
from models.experience_model import Job
from datetime import datetime

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


def load_models_paths(paths: List[str], model: Type[BaseModel]) -> List[BaseModel]:
    all_validated_models = []
    for path in paths:
        validated_models = load_models(path, model)
        all_validated_models.extend(validated_models)

    return all_validated_models


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
                print(file_path)
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")

    if model == Job:  # Ensure sorting only applies to Job models
        validated_models.sort(
            key=lambda x: datetime.strptime(x.start_date, "%m/%y"), reverse=True
        )

    return validated_models


def load_model_from_dir(directory: str, model: Type[BaseModel]) -> BaseModel:
    """
    Loads a model from JSON files in a specified directory. Each file corresponds to
    a field in the model.

    Args:
    - directory: The base directory containing the model data.
    - model: The Pydantic model class to instantiate.

    Returns:
    - An instance of the specified model class, populated with data from the directory.
    """
    data = {}
    for field in model.__fields__.keys():
        file_path = os.path.join(directory, f"{field}.json")
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                data[field] = json.load(file)
        else:
            print(f"No data found for {field} at {file_path}, skipping.")

    try:
        return model(**data)
    except ValidationError as e:
        raise ValueError(f"Error loading model {model.__name__}: {str(e)}")
