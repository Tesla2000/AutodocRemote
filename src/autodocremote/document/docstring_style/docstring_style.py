from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from typing import Iterable
from typing import Optional


class DocstringStyle(ABC):
    type: str

    def __init__(
        self, indentation_length: int, line_length: int, tab_length: int, **_
    ):
        self.indentation_length = indentation_length
        self.tab_length = tab_length
        self.line_length = line_length

    @abstractmethod
    def generate(
        self,
        summary: str,
        parameters: Iterable[str],
        returns: str,
        missing_parameters: Iterable[str],
        actual_parameters: dict[str, str],
        expected_parameters: Iterable[str],
    ) -> str:
        pass

    def _split_line(
        self, line: str, indentation_length: Optional[int] = None
    ) -> str:
        if indentation_length is None:
            indentation_length = self.indentation_length
        line = line.split()
        new_lines = [[]]
        tab = indentation_length * " "
        for word in line:
            last_line = new_lines[-1]
            if last_line and (
                sum(map(len, last_line)) + len(word) + len(last_line)
                > self.line_length - indentation_length
            ):
                new_lines[-1] = " ".join(new_lines[-1])
                new_lines.append([])
            new_lines[-1].append(word)
        new_lines[-1] = " ".join(new_lines[-1])
        return "".join(map((tab + "{}\n").format, new_lines))
