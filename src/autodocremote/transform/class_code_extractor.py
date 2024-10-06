from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

import libcst as cst
from autodocremote.transform.class_structure_extractor import (
    ClassStructureExtractor,
)
from libcst import ClassDef
from libcst import Module


class ClassCodeExtractor:
    def __init__(self):
        self.imported_elements = {}
        self.defined_classes = {}

    def extract(self, node: "ClassDef"):
        class_name = node.name.value
        bases = tuple(base.value.value for base in node.bases)
        base_classes = "".join(filter(None, map(self._get_class_code, bases)))
        class_code = (
            base_classes.strip() + "\n\n" + Module(body=[node]).code.strip()
        )
        self.defined_classes[class_name] = class_code
        return class_code

    def _get_class_code(self, class_name: str) -> Optional[str]:
        if class_name in self.defined_classes:
            return self.defined_classes[class_name]
        if class_name not in self.imported_elements:
            return
        class_module = self.imported_elements[class_name].module
        if isinstance(class_module.value, str):
            from_string = class_module.value
        else:
            from_string = os.path.join(
                class_module.value.value, class_module.attr.value
            )
        current_working_directory = os.getcwd()
        parent_path = Path(
            os.path.join(current_working_directory, from_string)
        ).with_suffix(".py")
        if not parent_path.exists():
            return Module([self.imported_elements[class_name]]).code
        code = parent_path.read_text()
        module = cst.parse_module(code)
        transformer = ClassStructureExtractor(module)
        module.visit(transformer)
        return transformer.class_code_extractor.defined_classes.get(class_name)
