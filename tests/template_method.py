from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class Programmer(ABC):
    def live(self):
        """
        Continuously executes the sleep, eat, and code methods in an infinite
        loop, simulating the daily routine of a programmer.
        :return: None
        """
        while True:
            self._sleep()
            self._eat()
            self._code()

    @abstractmethod
    def _sleep(self):
        """
        Defines an abstract method for sleeping behavior in a Programmer class.
        :return: None
        """

    @abstractmethod
    def _eat(self):
        """
        Defines an abstract method for eating behavior that must be implemented
        by subclasses.
        :return: None
        """

    @abstractmethod
    def _code(self):
        """
        Defines an abstract method for coding behavior that must be implemented
        by subclasses.
        :return: None
        """
