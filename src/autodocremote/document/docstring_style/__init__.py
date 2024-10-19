from __future__ import annotations

from importlib import import_module
from pathlib import Path


def import_python(root: Path):
    """
    The `import_python` function recursively imports Python modules from a
    specified directory, excluding certain files like `__init__.py` and
    `pycache`. It yields the names of the imported modules while maintaining
    their relative paths within the directory structure.
    :param root: A `Path` object representing the directory from which Python
    modules will be imported recursively.
    :return: Yields the names of imported Python modules found in the specified
    directory and its subdirectories.
    """
    for module_path in root.iterdir():
        if module_path.name in ("__init__.py", "pycache", "__pycache__"):
            continue
        if module_path.is_file():
            relative_path = module_path.relative_to(Path(__file__).parent)
            subfolders = "".join(map(".{}".format, relative_path.parts[:-1]))
            str_path = module_path.with_suffix("").name
            import_module("." + str_path, __name__ + subfolders)
            yield module_path.with_suffix("").name
            continue
        yield from import_python(module_path)


__all__ = list(import_python(Path(__file__).parent))
