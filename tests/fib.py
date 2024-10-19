from __future__ import annotations


def fibonacci_doc(n: int) -> int:
    """
    Calculates the nth Fibonacci number, where the sequence starts with 0 and
    1.
    :param n: The position in the Fibonacci sequence to retrieve, must be a
    positive integer.
    :return: The nth Fibonacci number.
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


def fibonacci(n, a: int = 0, b: int = 1, c: int = 2) -> int:
    """
    Calculates the n-th Fibonacci number using an iterative approach with
    customizable starting values.

    Args:
        n (object): The position in the Fibonacci sequence to retrieve, must be
        a positive integer.
        a (int): The first number in the Fibonacci sequence, default is 0.
        b (int): The second number in the Fibonacci sequence, default is 1.
        c (int): The index for the Fibonacci sequence, starting from 2.

    Returns:
        The n-th Fibonacci number.
    """
    if n <= 0:
        raise ValueError("The input must be a positive integer.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    for _ in range(2, n):
        a, b = b, a + b
    return b
