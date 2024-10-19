from __future__ import annotations

from itertools import filterfalse
from typing import Sequence
from typing import Type

from libcst import FunctionDef
from libcst import Module

from ..config import Config
from .docstring_parameter_extractors import DocstringParametersExtractor
from .docstring_style.docstring_style import DocstringStyle
from .generate_descriptions import generate_descriptions


class FunctionDocstringGenerator:
    actual_parameters: dict[str, str]
    missing_parameters: Sequence[str]
    indentation_length: int
    expected_parameters: tuple[str, ...]
    parameter_types: dict[str, str]
    doc: str

    def __init__(
        self,
        original_node: FunctionDef,
        config: Config,
        docstring_style: Type[DocstringStyle],
    ):
        """
        The `__init__` function initializes an instance by accepting an
        `original_node` of type `FunctionDef` and a `config` of type `Config`,
        storing them as instance attributes for further use.
        :param original_node: A representation of the original function
        definition being processed or modified.
        :param config: An instance of the Config class that contains
        configuration settings used to initialize the function.
        :return: An instance of the class initialized with the given function
        definition and configuration.
        """
        self.docstring_style = docstring_style
        self.config = config
        self.original_node = original_node

    def is_valid(self, indentation_level: int) -> bool:
        """
        The `is_valid` function checks the validity of a docstring by comparing
        the expected parameters of a function against those documented within
        the docstring, considering indentation and configuration settings. It
        returns `True` if there are missing parameters or if the docstring is
        absent, and `False` otherwise.
        :param indentation_level: Specifies the level of indentation for
        formatting the parameters in the function's docstring, influencing how
        the parameters are represented in the output.
        :return: Returns `True` if there are missing parameters or if the
        docstring is absent; otherwise, returns `False`.
        """
        self.expected_parameters = tuple(
            param.name.value
            for param in self.original_node.params.params
            if param.name.value != "self"
        )
        self.parameter_types = {
            param.name.value: (
                param.annotation and param.annotation.annotation.value
            )
            or "object"
            for param in self.original_node.params.params
            if param.name.value != "self"
        }
        self.indentation_length = indentation_level * self.config.tab_length
        tab = self.indentation_length * " "
        self.doc = self.original_node.get_docstring()
        if self.doc:
            self.actual_parameters = DocstringParametersExtractor.extract_all(
                self.doc, tab
            )
        else:
            self.actual_parameters = {}
        if self.doc and not self.config.update_overwrite:
            return False
        self.missing_parameters = tuple(
            filterfalse(
                self.actual_parameters.keys().__contains__,
                self.expected_parameters,
            )
        )
        if not self.missing_parameters and self.doc:
            return False
        return True

    def generate(self, class_code: str = "") -> str:
        """
        The `generate` function creates a formatted docstring by extracting and
        processing a summary, parameters, and result descriptions from a code
        module, while handling missing parameters and applying line length and
        indentation configurations. It returns the constructed docstring as a
        formatted string.
        :return: A formatted docstring containing a summary, parameters, and
        result.
        """
        code = Module(body=[self.original_node]).code
        summary, parameters, result = generate_descriptions(
            code, self.missing_parameters, self.config, class_code
        )
        return self.docstring_style(
            self.indentation_length,
            self.config.line_length,
            self.config.tab_length,
            parameter_types=self.parameter_types,
        ).generate(
            summary,
            parameters,
            result,
            self.missing_parameters,
            self.actual_parameters,
            self.expected_parameters,
        )
