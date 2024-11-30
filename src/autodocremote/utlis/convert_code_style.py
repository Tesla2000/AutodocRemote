from __future__ import annotations

from pathlib import Path

from pyment import PyComment

from ..document.docstring_style import DocstringStyle


def convert_docstring_style(
    filepath: Path | str, style: DocstringStyle
) -> int:
    c = PyComment(str(filepath), output_style=style.value)
    c.proceed()
    list_from, list_to = c.compute_before_after()
    lines_to_write = list_to
    if list_from != list_to:
        code = filepath.read_text()
        c.overwrite_source_file(lines_to_write)
        new_code = filepath.read_text()
        if new_code != code:
            print(f"File {filepath} was modified")
            return 1
    return 0
