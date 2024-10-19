# flake8: noqa
from __future__ import annotations

from contextlib import nullcontext

with nullcontext():

    def foo():
        """
        The function `foo` contains a nested function `fibonacci` that computes
        the nth Fibonacci number, raising a ValueError for non-positive integer
        inputs and returning 0 for the first Fibonacci number and 1 for the
        second. It uses an iterative approach to calculate the Fibonacci
        sequence for values of n greater than 2.
        :return: The nth Fibonacci number.
        """

        def fibonacci(n, a: int = 0, b: int = 1) -> int:
            """
            The `fibonacci` function computes the n-th Fibonacci number, where
            the sequence starts with 0 and 1, and raises a ValueError for
            non-positive integer inputs. It uses an iterative approach to
            efficiently calculate the result for positive integers greater than
            1.
            :param a: An integer representing the first number in the Fibonacci
            sequence, initialized to 0 by default.
            :param b: An integer representing the second number in the
            Fibonacci sequence, which is initialized to 1 and updated during
            the computation of the sequence.
            :param n: A positive integer representing the position in the
            Fibonacci sequence to retrieve, where the sequence starts with 0 at
            position 1 and 1 at position 2.
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


try:

    def foo():
        """
        The function `foo` contains a nested function `fibonacci` that
        calculates the nth Fibonacci number, raising an error for non-positive
        integer inputs and returning 0 for the first Fibonacci number and 1 for
        the second. It uses an iterative approach to compute the Fibonacci
        sequence for values of n greater than 2.
        :return: the nth Fibonacci number
        """

        def fibonacci(n, a: int = 0, b: int = 1) -> int:
            """
            The `fibonacci` function computes the nth Fibonacci number, where
            the sequence starts with 0 and 1, and raises a ValueError for
            non-positive integer inputs. It iteratively calculates the
            Fibonacci numbers using two variables to track the current and
            previous values in the sequence.
            :param a: An integer representing the first number in the Fibonacci
            sequence, initialized to 0 by default.
            :param b: An integer representing the second number in the
            Fibonacci sequence, which is used to calculate subsequent Fibonacci
            numbers.
            :param n: A positive integer representing the position in the
            Fibonacci sequence to retrieve, where the sequence starts with 0 at
            position 1 and 1 at position 2.
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

except Exception as e:

    def foo():
        """
        The function `foo` contains a nested function `fibonacci` that
        calculates the n-th Fibonacci number, raising an error for non-positive
        integers and returning the appropriate Fibonacci values for inputs 1
        and 2. For values of n greater than 2, it iteratively computes the
        Fibonacci sequence using two variables to track the last two numbers.
        :return: the nth Fibonacci number
        """

        def fibonacci(n, a: int = 0, b: int = 1) -> int:
            """
            The `fibonacci` function computes the n-th Fibonacci number, where
            the first two Fibonacci numbers are defined as 0 and 1. It raises a
            ValueError for non-positive integer inputs and uses an iterative
            approach to calculate the result for valid inputs.
            :param a: An integer representing the first number in the Fibonacci
            sequence, initialized to 0 by default.
            :param b: Specifies the second number in the Fibonacci sequence,
            which is initialized to 1 by default.
            :param n: A positive integer representing the position in the
            Fibonacci sequence to retrieve, where the sequence starts with 0 at
            position 1 and 1 at position 2.
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

else:

    def foo():
        """
        The function `foo` contains a nested function `fibonacci` that
        calculates the nth Fibonacci number, where n must be a positive
        integer. It raises a ValueError for non-positive inputs and returns the
        Fibonacci number based on the standard sequence.
        :return: the nth Fibonacci number
        """

        def fibonacci(n, a: int = 0, b: int = 1) -> int:
            """
            The `fibonacci` function calculates the n-th Fibonacci number,
            where the sequence starts with 0 and 1, and raises a ValueError if
            the input is not a positive integer. It uses an iterative approach
            to compute the result efficiently.
            :param a: An integer representing the first number in the Fibonacci
            sequence, initialized to 0 by default.
            :param b: An integer representing the second number in the
            Fibonacci sequence, initialized to 1 by default.
            :param n: A positive integer representing the position in the
            Fibonacci sequence to retrieve, where the sequence starts with 0 at
            position 1 and 1 at position 2.
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

finally:

    def foo():
        """
        The function `foo` contains a nested function `fibonacci` that computes
        the n-th Fibonacci number, where n must be a positive integer. It
        raises a ValueError for non-positive inputs and returns 0 for the first
        Fibonacci number and 1 for the second.
        :return: the nth Fibonacci number
        """

        def fibonacci(n, a: int = 0, b: int = 1) -> int:
            """
            The `fibonacci` function computes the n-th Fibonacci number, where
            the sequence starts with 0 and 1, and raises a ValueError for
            non-positive integer inputs. It uses an iterative approach to
            efficiently calculate the result for n greater than 2.
            :param a: An integer representing the first number in the Fibonacci
            sequence, initialized to 0 by default.
            :param b: An integer that represents the current Fibonacci number
            in the sequence, initialized to 1 for the calculation.
            :param n: A positive integer representing the position in the
            Fibonacci sequence to retrieve, where the sequence starts with 0 at
            position 1 and 1 at position 2.
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


if True:

    def foo():
        """
        The function `foo` contains a nested function `fibonacci` that
        calculates the n-th Fibonacci number, raising an error for non-positive
        integer inputs and returning 0 for the first Fibonacci number and 1 for
        the second. It uses an iterative approach to compute the Fibonacci
        sequence for values of n greater than 2.
        :return: the nth Fibonacci number
        """

        def fibonacci(n, a: int = 0, b: int = 1) -> int:
            """
            Calculates the nth Fibonacci number using an iterative approach.

            Args:
                n (object): The position in the Fibonacci sequence to
                calculate, must be a positive integer.
                a (int): The first number in the Fibonacci sequence, default is
                0.
                b (int): The second number in the Fibonacci sequence, default
                is 1.

            Returns:
                The nth Fibonacci number.
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

elif False:

    def foo():
        """
        The function `foo` contains a nested function `fibonacci` that
        calculates the n-th Fibonacci number, where `n` must be a positive
        integer. It raises a ValueError for non-positive inputs and returns 0
        for the first Fibonacci number and 1 for the second.
        :return: the nth Fibonacci number
        """

        def fibonacci(n, a: int = 0, b: int = 1) -> int:
            """
            The `fibonacci` function calculates the n-th Fibonacci number,
            where the sequence starts with 0 and 1, and raises a ValueError if
            the input is not a positive integer. It uses an iterative approach
            to compute the result efficiently.
            :param a: An integer that represents the first number in the
            Fibonacci sequence, initialized to 0 by default.
            :param b: An integer representing the second number in the
            Fibonacci sequence, which is initialized to 1 and updated during
            the computation of the sequence.
            :param n: A positive integer representing the position in the
            Fibonacci sequence to retrieve, where the sequence starts with 0 at
            position 1 and 1 at position 2.
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

else:

    def foo():
        """
        The function `foo` contains a nested function `fibonacci` that computes
        the n-th Fibonacci number, where n must be a positive integer. It
        raises a ValueError for non-positive inputs and returns 0 for the first
        Fibonacci number and 1 for the second.
        :return: the nth Fibonacci number
        """

        def fibonacci(n, a: int = 0, b: int = 1) -> int:
            """
            The `fibonacci` function calculates the n-th Fibonacci number,
            where the first two numbers in the sequence are defined as 0 and 1.
            It raises a ValueError if the input is not a positive integer.
            :param a: An integer representing the first number in the Fibonacci
            sequence, initialized to 0 by default.
            :param b: An integer representing the current Fibonacci number in
            the sequence, initialized to 1 for the calculation.
            :param n: A positive integer representing the position in the
            Fibonacci sequence to retrieve, where the sequence starts with 0 at
            position 1 and 1 at position 2.
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


for _ in range(0):

    def foo():
        """
        The function `foo` contains a nested function `fibonacci` that computes
        the nth Fibonacci number, raising an error for non-positive integer
        inputs and returning 0 for the first Fibonacci number and 1 for the
        second. It uses an iterative approach to calculate the Fibonacci
        sequence for values of n greater than 2.
        :return: the nth Fibonacci number
        """

        def fibonacci(n, a: int = 0, b: int = 1) -> int:
            """
            The `fibonacci` function computes the nth Fibonacci number, where
            the sequence starts with 0 and 1, and raises a ValueError for
            non-positive integer inputs. It uses an iterative approach to
            efficiently calculate the result.
            :param a: An integer representing the first number in the Fibonacci
            sequence, initialized to 0 by default.
            :param b: An integer that represents the current Fibonacci number
            in the sequence during the iterative calculation.
            :param n: A positive integer representing the position in the
            Fibonacci sequence to retrieve, where the sequence starts with 0 at
            position 1 and 1 at position 2.
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

else:

    def foo():
        """
        The function `foo` contains a nested function `fibonacci` that
        calculates the nth Fibonacci number, where n must be a positive
        integer. It raises a ValueError for non-positive inputs and returns 0
        for n=1 and 1 for n=2, while using an iterative approach for larger
        values of n.
        :return: the nth Fibonacci number
        """

        def fibonacci(n, a: int = 0, b: int = 1) -> int:
            """
            The `fibonacci` function calculates the n-th Fibonacci number,
            where the sequence starts with 0 and 1, and raises a ValueError for
            non-positive integer inputs. It uses an iterative approach to
            compute the result efficiently.
            :param a: An integer representing the first number in the Fibonacci
            sequence, initialized to 0 by default.
            :param b: The parameter b represents the second number in the
            Fibonacci sequence and is used to calculate subsequent Fibonacci
            numbers during the iteration.
            :param n: A positive integer representing the position in the
            Fibonacci sequence to retrieve, where the sequence starts with 0 at
            position 1 and 1 at position 2.
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


class Foo:
    def foo(self):
        """
        The function `foo` contains a nested function `fibonacci` that computes
        the nth Fibonacci number, raising an error for non-positive integer
        inputs and returning the appropriate Fibonacci values for the first two
        positions. It uses an iterative approach to calculate the Fibonacci
        sequence, starting from 0 and 1.
        :return: The nth Fibonacci number.
        """

        def fibonacci(n, a: int = 0, b: int = 1) -> int:
            """
            The `fibonacci` function computes the n-th Fibonacci number, where
            the first two Fibonacci numbers are defined as 0 and 1. It raises a
            ValueError if the input is not a positive integer and uses an
            iterative approach to calculate the result for n greater than 2.
            :param a: An integer representing the first number in the Fibonacci
            sequence, initialized to 0 by default.
            :param b: An integer representing the second number in the
            Fibonacci sequence, initialized to 1 by default.
            :param n: A positive integer representing the position in the
            Fibonacci sequence to retrieve, where the sequence starts with 0 at
            position 1 and 1 at position 2.
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


def foo():
    """
    The function `foo` contains a nested function `fibonacci` that computes the
    nth Fibonacci number, where n must be a positive integer. It raises a
    ValueError for non-positive inputs and returns 0 for the first Fibonacci
    number and 1 for the second.
    :return: the nth Fibonacci number
    """

    def fibonacci(n, a: int = 0, b: int = 1) -> int:
        """
        The `fibonacci` function computes the n-th Fibonacci number, where the
        sequence starts with 0 and 1, and raises a ValueError if the input is
        not a positive integer. It uses an iterative approach to calculate the
        Fibonacci number efficiently.
        :param a: An integer representing the first number in the Fibonacci
        sequence, which is used as a starting point for the calculation.
        :param b: The parameter b represents the second number in the Fibonacci
        sequence, initialized to 1, and is used to calculate subsequent
        Fibonacci numbers during the iteration.
        :param n: A positive integer representing the position in the Fibonacci
        sequence to retrieve, where the sequence starts with 0 at position 1
        and 1 at position 2.
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
