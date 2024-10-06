from __future__ import annotations

from typing import Sequence

import libcst as cst
from libcst import Module


class Transformer(cst.CSTTransformer):

    def __init__(self, module: Module):
        """
        The `__init__` function initializes an instance of a class by accepting
        a `Module` and a `Config` object, storing them as instance attributes.
        It also calls the initializer of its superclass to ensure proper setup.
        :param module: An instance of the Module class that represents a
        specific component or layer in a neural network architecture.
        :return: An instance of the class initialized with the provided module
        and configuration.
        """
        super().__init__()
        self.module = module

    def _get_path_attrs(self, elem, attrs: Sequence[str]):
        """
        The `_get_path_attrs` function traverses a sequence of attributes from
        a given element, returning the final attribute's value if all
        attributes exist; otherwise, it returns `None`.
        :param elem: An object representing the starting point from which
        attributes will be accessed sequentially based on the provided list of
        attribute names.
        :param attrs: A sequence of attribute names used to traverse the
        hierarchy of an object, retrieving the final attribute's value if all
        specified attributes exist.
        :return: The final attribute value or None if any attribute is missing.
        """
        current_elem = elem
        for attr in attrs:
            if not hasattr(current_elem, attr):
                return
            current_elem = getattr(current_elem, attr)
        return current_elem

    def _set_path_attrs(self, elem, attrs: Sequence[str], **kwargs):
        """
        The `_set_path_attrs` function updates the attributes of a nested
        element within a given structure by retrieving the specified path and
        applying changes to it, ultimately returning the modified inner
        element. It iteratively adjusts the outer elements by incorporating the
        updated inner element at each level of the specified attribute path.
        :param elem: An element representing a specific node or object in a
        data structure that the function will modify by setting attributes.
        :param attrs: A sequence of attribute names that specify the
        hierarchical path for which attributes are being set in the given
        element.
        :return: A modified inner element with updated attributes.
        """
        inner_element = self._get_path_attrs(elem, attrs)
        inner_element = inner_element.with_changes(**kwargs)
        for i in range(1, len(attrs) + 1):
            outer_element = self._get_path_attrs(elem, attrs[:-i])
            inner_element = outer_element.with_changes(
                **{attrs[-i]: inner_element}
            )
        return inner_element
