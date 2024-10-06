from __future__ import annotations

from libcst import ClassDef
from libcst import Else
from libcst import ExceptHandler
from libcst import Finally
from libcst import For
from libcst import FunctionDef
from libcst import If
from libcst import Module
from libcst import Try
from libcst import With
from libcst.matchers import ImportFrom

from .transformer import Transformer

indented_children = (
    ClassDef,
    FunctionDef,
    If,
    For,
    Try,
    With,
    ExceptHandler,
    Else,
    Finally,
)


class ClassStructureExtractor(Transformer):
    def __init__(self, module: Module):
        """
        The `__init__` function initializes an instance of a class by calling
        its superclass constructor with a given module and configuration, while
        also setting up a `defaultdict` to track indentation levels, defaulting
        to 1. This allows for dynamic management of indentation levels within
        the class.
        :param config: A configuration object that provides settings and
        parameters for initializing the module.
        :param module: Represents a specific component or layer
        of a neural network that the class will utilize for processing and
        configuration.
        :return: A dictionary with default indentation levels set to 1.
        """
        from .class_code_extractor import ClassCodeExtractor

        super().__init__(module)
        self.class_code_extractor = ClassCodeExtractor()

    def visit_ClassDef_body(self, node: "ClassDef") -> None:
        parents = self.class_code_extractor.extract(node)
        self.class_code_extractor.defined_classes[node.name.value] = parents
        super().visit_ClassDef_body(node)

    def visit_ImportFrom(self, node: "ImportFrom") -> None:
        for import_alias in node.names:
            self.class_code_extractor.imported_elements[
                import_alias.name.value
            ] = node
