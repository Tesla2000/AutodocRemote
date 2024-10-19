from __future__ import annotations

from autodocremote.document.docstring_parameter_extractors.docstring_parameters_extractor import (  # noqa: E501
    DocstringParametersExtractor,
)


class PlainDocstringParametersExtractor(DocstringParametersExtractor):
    @classmethod
    def extract(cls, docstring: str, tab: str) -> dict[str, str]:
        return dict(
            (
                (partition := param.partition(":"))[0],
                f"{tab}:param {partition[0]}:{partition[2]}",
            )
            for param in docstring.rpartition(":return:")[0].split(":param ")[
                1:
            ]
        )
