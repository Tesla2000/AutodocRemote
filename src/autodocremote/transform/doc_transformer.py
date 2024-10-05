from __future__ import annotations

from collections import defaultdict

from libcst import ClassDef
from libcst import Else
from libcst import ExceptHandler
from libcst import Expr
from libcst import Finally
from libcst import For
from libcst import FunctionDef
from libcst import If
from libcst import IndentedBlock
from libcst import Module
from libcst import SimpleStatementLine
from libcst import SimpleString
from libcst import Try
from libcst import With

from ..config import Config
from ..document.function_docstring_generator import FunctionDocstringGenerator
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


class DocTransformer(Transformer):
    def __init__(self, module: Module, config: Config):
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
        super().__init__(module, config)
        self.indentation_levels = defaultdict(lambda: 1)
        self.function_parents = {}

    def leave_FunctionDef(
        self, original_node: "FunctionDef", updated_node: "FunctionDef"
    ) -> "FunctionDef":
        """
        The `leave_FunctionDef` function updates a given function definition
        node by generating and inserting a docstring based on the original
        node, provided that the generated docstring is valid according to the
        specified indentation level. If the docstring is not valid, it returns
        the original function definition unchanged.
        :param original_node: A `FunctionDef` node representing the original
        function definition that may be updated with a generated docstring.
        :param updated_node: A "FunctionDef" node that represents the updated
        version of the original function definition, which may incorporate a
        generated docstring.
        :return: Returns the updated function definition with a generated
        docstring, or the original if invalid.
        """
        indentation_level = self.indentation_levels[original_node]
        generator = FunctionDocstringGenerator(original_node, self.config)
        if not generator.is_valid(indentation_level):
            return original_node
        result_doc = generator.generate(
            self.function_parents.get(original_node, "")
        )
        expr = Expr(value=SimpleString(value=result_doc))
        statement_line = SimpleStatementLine(body=(expr,))
        path_attrs = self._get_path_attrs(updated_node, ["body", "body"])
        path_attrs = path_attrs[bool(generator.doc) :]
        body = (statement_line, *path_attrs)
        return self._set_path_attrs(updated_node, ["body"], body=body)

    def visit_ClassDef_body(self, node: "ClassDef") -> None:
        for child in node.body.body:
            if not isinstance(child, FunctionDef):
                continue
            self.function_parents[child] = Module(body=[node]).code.strip()
        super().visit_ClassDef_body(node)

    def visit_IndentedBlock_body(self, node: "IndentedBlock") -> None:
        """
        The `visit_IndentedBlock_body` function processes the children of an
        `IndentedBlock` node, updating their indentation levels if they are
        instances of `IndentedBlock`, `ClassDef`, or `FunctionDef`. It then
        calls the superclass method to ensure any additional processing is
        handled.
        :param node: Represents an instance of an indented block in the code
        structure, containing a list of child nodes that may include other
        indented blocks, class definitions, or function definitions.
        :return: A dictionary mapping child nodes to their indentation levels.
        """
        for child in node.body:
            if not isinstance(child, indented_children):
                continue
            self.indentation_levels[child] = self.indentation_levels[node] + 1
            self.indentation_levels[child.body] = (
                self.indentation_levels[node] + 1
            )
        super().visit_IndentedBlock_body(node)
