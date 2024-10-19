from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from collections import ChainMap


class DocstringParametersExtractor(ABC):
    @classmethod
    @abstractmethod
    def extract(cls, docstring: str, tab: str) -> dict[str, str]:
        pass

    @classmethod
    def extract_all(cls, docstring: str, tab: str) -> dict[str, str]:
        return dict(
            ChainMap(
                *tuple(
                    class_.extract(docstring, tab)
                    for class_ in cls.__subclasses__()
                )
            )
        )
