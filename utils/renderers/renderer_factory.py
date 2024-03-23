from .jinja2_renderer import Jinja2Renderer


def get_renderer(format: str):
    if format == "jinja2":
        return Jinja2Renderer()
    else:
        raise ValueError(f"Unsupported format: {format}")
