from __future__ import annotations


class FibCalculatorDoc:
    def fibonacci_doc(n: int) -> int:
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


class FibCalculator:
    def fibonacci(n, a: int = 0, b: int = 1) -> int:
        """
        The `fibonacci` function calculates the nth Fibonacci number, where the
        sequence starts with 0 and 1, and raises a ValueError for non-positive
        integer inputs. It uses an iterative approach to compute the Fibonacci
        value efficiently.
        :param b: Specifies the second number in the Fibonacci sequence, which
        is initialized to 1 by default.
        :param n: A positive integer representing the position in the Fibonacci
        sequence to retrieve, where the sequence starts with 0 at position 1
        and 1 at position 2.
        :param a: An integer representing the first number in the Fibonacci
        sequence, initialized to 0 by default.
        :return: The nth Fibonacci number.
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
