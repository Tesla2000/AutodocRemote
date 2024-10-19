from __future__ import annotations

from typing import Type

from autodocremote.document.docstring_style.docstring_style import (
    DocstringStyle,
)


class DocstringStyleFactory:
    @classmethod
    def create(cls, type: str) -> Type[DocstringStyle]:
        for class_ in DocstringStyle.__subclasses__():
            if class_.type == type:
                return class_
        raise ValueError(f"Invalid docstring type {type}")
