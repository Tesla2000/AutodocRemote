from __future__ import annotations

from functools import partial
from typing import Iterable
from typing import Literal

from autodocremote.document.docstring_style.docstring_style import (
    DocstringStyle,
)


class GoogleStyle(DocstringStyle):
    type: Literal["google"] = "google"

    def __init__(
        self,
        indentation_length: int,
        line_length: int,
        tab_length: int,
        parameter_types: dict[str, str],
        **_,
    ):
        super().__init__(indentation_length, line_length, tab_length, **_)
        self.parameter_types = parameter_types

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
            tuple(
                map(
                    partial(
                        self._split_line,
                        indentation_length=self.indentation_length
                        + self.tab_length,
                    ),
                    parameters,
                )
            ),
            self._split_line(
                result,
                indentation_length=self.indentation_length + self.tab_length,
            ),
        )
        parameters = dict(zip(missing_parameters, parameters))
        parameters.update(actual_parameters)
        tab = self.indentation_length * " "
        param_lines = "".join(
            parameters[parameter] for parameter in expected_parameters
        )

        return (
            '"""\n{}{}\n'.format(
                summary + "\n" + tab + "Args:\n" if param_lines else summary,
                param_lines,
            )
            + tab
            + f'Returns:\n{result}{tab}"""'
        )

    def _conv2docstring_lines(
        self,
        parameters: Iterable[str],
        return_value: str,
        parameter_names: Iterable[str],
    ) -> tuple[tuple[str, ...], str]:
        tab = self.tab_length * " "
        return (
            tuple(
                f"{tab}{name} ({self.parameter_types[name]}): {description}"
                for name, description in zip(parameter_names, parameters)
            ),
            f"{tab}{return_value}",
        )
