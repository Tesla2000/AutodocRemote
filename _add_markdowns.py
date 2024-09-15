from __future__ import annotations

from pathlib import Path

additional_documents_header = """Additional Documentation
------------------------

.. toctree::
   :maxdepth: 2
   :caption: Contents:"""


def add_markdowns():
    """
    The `add_markdowns` function updates reStructuredText (.rst) files in the
    "docs/source" directory by appending a list of relative paths to Markdown
    (.md) files found in corresponding subdirectories, excluding specific files
    like "index.rst" and "modules.rst." It constructs the additional
    documentation section by reading the existing content, formatting the new
    paths, and writing the updated content back to the original .rst files.
    :return: A string representing the relative path of a markdown file without
    its suffix.
    """

    def _conv2ref(markdown_file_path: Path) -> str:
        """
        The function `_conv2ref` takes a file path to a Markdown file and
        returns its relative path to a specified source directory, removing the
        file extension. It converts the input `Path` object to a string format,
        ensuring that the resulting path does not include the suffix.
        :param markdown_file_path: A Path object representing the location of a
        markdown file, used to generate a relative reference string without its
        file extension.
        :return: A relative path string without the file extension.
        """
        return str(markdown_file_path.relative_to(source_path).with_suffix(""))

    source_path = Path("docs/source")
    for file in source_path.glob("*.rst"):
        if file.name in ("index.rst", "modules.rst"):
            continue
        content = file.read_text()
        before, _, after = content.rpartition(additional_documents_header)
        before = (before or after).rstrip()
        documentation_path = "/".join(file.name.split(".")[:-1])
        markdown_files = source_path.joinpath(documentation_path).rglob("*.md")
        indent = 3 * " "
        additional_docs = f"\n{indent}".join(map(_conv2ref, markdown_files))
        file.write_text(
            "{}\n{}\n\n{}{}\n".format(
                before, additional_documents_header, indent, additional_docs
            )
        )


if __name__ == "__main__":
    add_markdowns()
