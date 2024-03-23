import os


def parse_template_format(template_name: str) -> str:
    _, extension = os.path.splitext(template_name)

    if extension in [".jinja"]:
        return "jinja2"
    else:
        raise ValueError(f"Unsupported template format for file: {template_name}")
