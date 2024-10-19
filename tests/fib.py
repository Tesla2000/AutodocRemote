from __future__ import annotations


def fibonacci_doc(n: int) -> int:
    """
    Calculates the n-th Fibonacci number, where the sequence starts with 0 and
    1.
    :param n: The position in the Fibonacci sequence to retrieve, must be a
    positive integer.
    :return: The n-th Fibonacci number.
    """
    if n <= 0:
        raise ValueError("The input must be a positive integer.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b


def fibonacci(n, a: int = 0, b: int = 1) -> int:
    if n <= 0:
        raise ValueError("The input must be a positive integer.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    for _ in range(2, n):
        a, b = b, a + b
    return b
