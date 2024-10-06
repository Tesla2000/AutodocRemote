from __future__ import annotations

from tests.template_method import Programmer

# from tests.fib_class import FibCalculator
#
# class Foo:
#     """Does things"""
#
#
# class PythonProgrammer(Programmer, FibCalculator, Foo):
#     def _code(self):
#         print("Hello World")


class PythonProgrammer(Programmer):
    def _code(self):
        """
        Prints 'Hello World' to the console.
        :return: None
        """
        print("Hello World")
