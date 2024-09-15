from __future__ import annotations

from pathlib import Path

import libcst as cst

from ..config import Config
from .doc_transformer import DocTransformer


def modify_file(filepath: Path, config: Config) -> int:
    """
    The `modify_file` function reads the content of a specified file, applies a
    transformation using a configuration object, and writes the modified
    content back to the file if changes are detected, returning 1 for a
    modification and 0 otherwise.
    :param config: A configuration object that specifies the parameters and
    options for transforming the code within the specified file.
    :param filepath: A Path object representing the file to be modified by the
    function.
    :return: 1 if the file was modified, otherwise 0.
    """
    code = filepath.read_text()
    module = cst.parse_module(code)
    transformer = DocTransformer(module, config)
    new_code = module.visit(transformer).code
    if new_code != code:
        filepath.write_text(new_code)
        print(f"File {filepath} was modified")
        return 1
    return 0
