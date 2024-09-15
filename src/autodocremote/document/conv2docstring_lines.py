from __future__ import annotations

from typing import Sequence


def conv2docstring_lines(
    parameters: tuple[str, ...],
    return_value: str,
    missing_parameter_names: Sequence[str],
) -> tuple[tuple[str, ...], str]:
    """
    The `conv2docstring_lines` function generates formatted docstring lines for
    parameters and return values based on provided descriptions. It takes a
    tuple of parameter descriptions, a return value description, and a sequence
    of missing parameter names, returning a tuple containing the formatted
    parameter lines and the return line.
    :param missing_parameter_names: A sequence of parameter names that are
    missing descriptions, which will be paired with the provided descriptions
    in the output.
    :param return_value: A string that describes the value returned by the
    function.
    :param parameters: :param return_value: A string describing the return
    value of the function. :param missing_parameter_names: A sequence of
    parameter names that are missing descriptions.
    :return: A formatted string describing the return value of the function.
    """
    return (
        tuple(
            f":param {name}: {description}"
            for name, description in zip(missing_parameter_names, parameters)
        ),
        f":return: {return_value}",
    )
