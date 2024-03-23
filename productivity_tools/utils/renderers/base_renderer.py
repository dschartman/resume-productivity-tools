from abc import ABC, abstractmethod


class BaseRenderer(ABC):
    @abstractmethod
    def render(self, template_name: str, context: dict) -> str:
        pass
