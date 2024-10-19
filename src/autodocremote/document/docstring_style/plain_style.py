from __future__ import annotations

from typing import Iterable
from typing import Literal

from autodocremote.document.docstring_style.docstring_style import (
    DocstringStyle,
)


class PlainStyle(DocstringStyle):
    type: Literal["plain"] = "plain"

    def generate(
        self,
        summary: str,
        parameters: Iterable[str],
        returns: str,
        missing_parameters: Iterable[str],
        actual_parameters: dict[str, str],
        expected_parameters: Iterable[str],
    ) -> str:
        parameters, result = self._conv2docstring_lines(
            parameters, returns, missing_parameters
        )
        summary, parameters, result = (
            self._split_line(summary),
            tuple(map(self._split_line, parameters)),
            self._split_line(result),
        )
        parameters = dict(zip(missing_parameters, parameters))
        parameters.update(actual_parameters)
        return '"""{}{}{}"""'.format(
            "\n" + summary,
            "".join(map(parameters.get, expected_parameters)),
            result + self.indentation_length * " ",
        )

    @staticmethod
    def _conv2docstring_lines(
        parameters: Iterable[str],
        return_value: str,
        parameter_names: Iterable[str],
    ) -> tuple[tuple[str, ...], str]:
        return (
            tuple(
                f":param {name}: {description}"
                for name, description in zip(parameter_names, parameters)
            ),
            f":return: {return_value}",
        )
