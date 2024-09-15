from __future__ import annotations

from functools import partial
from typing import Sequence

from libcst import FunctionDef
from libcst import Module

from ..config import Config
from .conv2docstring_lines import conv2docstring_lines
from .generate_descriptions import generate_descriptions
from .split_lines import split_lines


class DocstringGenerator:
    actual_parameters: dict[str, str]
    missing_parameters: Sequence[str]
    indentation_length: int
    expected_parameters: set[str]
    doc: str

    def __init__(self, original_node: FunctionDef, config: Config):
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
        self.expected_parameters = set(
            param.name.value for param in self.original_node.params.params
        ) - {"self"}
        self.indentation_length = indentation_level * self.config.tab_length
        tab = self.indentation_length * " "
        self.doc = self.original_node.get_docstring()
        if self.doc:
            self.actual_parameters = dict(
                (
                    (partition := param.partition(":"))[0],
                    f"{tab}:param {partition[0]}:{partition[2]}",
                )
                for param in self.doc.rpartition(":return:")[0].split(
                    ":param "
                )[1:]
            )
        else:
            self.actual_parameters = {}
        if self.doc and not self.config.update_overwrite:
            return False
        self.missing_parameters = tuple(
            self.expected_parameters - set(self.actual_parameters.keys())
        )
        if not self.missing_parameters and self.doc:
            return False
        return True

    def generate(self) -> str:
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
            code, self.missing_parameters, self.config
        )
        parameters, result = conv2docstring_lines(
            parameters, result, self.missing_parameters
        )
        line_splitter = partial(
            split_lines,
            line_length=self.config.line_length,
            indentation_length=self.indentation_length,
        )
        summary, parameters, result = (
            line_splitter(summary),
            tuple(map(line_splitter, parameters)),
            line_splitter(result),
        )
        parameters = dict(zip(self.missing_parameters, parameters))
        parameters.update(self.actual_parameters)
        return '"""{}{}{}"""'.format(
            "\n" + summary,
            "".join(map(parameters.get, self.expected_parameters)),
            result + self.indentation_length * " ",
        )
