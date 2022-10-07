from abc import ABC, abstractmethod
from typing import List

from .Cat import Cat


class ImportInterface(ABC):

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[Cat]:
        pass
