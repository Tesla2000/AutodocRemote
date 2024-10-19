from __future__ import annotations

import re

from autodocremote.document.docstring_parameter_extractors.docstring_parameters_extractor import (  # noqa: E501
    DocstringParametersExtractor,
)


class GoogleDocstringParametersExtractor(DocstringParametersExtractor):
    @classmethod
    def extract(cls, docstring: str, tab: str) -> dict[str, str]:
        args = docstring.partition("\n\nArgs:\n")[-1].rpartition("\n\nReturn")[
            0
        ]
        match = r"\s*\w+[\ A-Za-z()]+:"
        arg_names = tuple(
            parameter.strip() for parameter in re.findall(match, args)
        )
        arg_descriptions = re.split(match, args)[-len(arg_names) :]
        return {
            key.split()[0]: tab + key + value + "\n"
            for key, value in zip(arg_names, arg_descriptions)
        }
