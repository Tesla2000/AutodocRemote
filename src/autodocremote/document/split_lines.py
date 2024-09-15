from __future__ import annotations


def split_lines(
    line: str, line_length: int = 79, indentation_length: int = 4
) -> str:
    """
    The `split_lines` function takes a string and formats it into multiple
    lines, ensuring that each line does not exceed a specified length while
    maintaining a consistent indentation. It splits the input text into words,
    wraps them according to the given line length, and adds indentation to each
    new line.
    :param indentation_length: Specifies the number of spaces to be used for
    indentation at the beginning of each new line in the formatted output.
    :param line: :param line_length: The maximum number of characters allowed
    per line, excluding indentation.
    :param line_length: Specifies the maximum number of characters allowed per
    line before a line break occurs, excluding indentation.
    :return: Formatted string with wrapped lines and indentation.
    """
    line = line.split()
    new_lines = [[]]
    tab = indentation_length * " "
    for word in line:
        last_line = new_lines[-1]
        if last_line and (
            sum(map(len, last_line)) + len(word) + len(last_line)
            > line_length - indentation_length
        ):
            new_lines[-1] = " ".join(new_lines[-1])
            new_lines.append([])
        new_lines[-1].append(word)
    new_lines[-1] = " ".join(new_lines[-1])
    return "".join(map((tab + "{}\n").format, new_lines))
