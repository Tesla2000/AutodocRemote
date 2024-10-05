from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class Programmer(ABC):
    def live(self):
        """
        Continuously executes the sleep, eat, and code methods in an infinite
        loop.
        :return: None
        """
        while True:
            self.sleep()
            self.eat()
            self.code()

    @abstractmethod
    def sleep(self):
        """
        Defines an abstract method for sleeping behavior in a Programmer class.
        :return: None
        """

    @abstractmethod
    def eat(self):
        """
        Defines an abstract method for eating behavior in a subclass of
        Programmer.
        :return: None
        """

    @abstractmethod
    def code(self):
        """
        Defines an abstract method for coding that must be implemented by
        subclasses of Programmer.
        :return: None
        """
