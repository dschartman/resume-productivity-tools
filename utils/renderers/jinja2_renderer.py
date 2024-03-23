from jinja2 import Environment, FileSystemLoader
from .base_renderer import BaseRenderer


class Jinja2Renderer(BaseRenderer):
    def __init__(self, templates_dir="templates/"):
        self.env = Environment(loader=FileSystemLoader(templates_dir))

    def render(self, template_name: str, context: dict) -> str:
        template = self.env.get_template(template_name)
        return template.render(context)
