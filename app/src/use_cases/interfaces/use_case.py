"""
Module containing the 'UseCase' Interface.
"""

from abc import ABC, abstractmethod


class UseCaseInterface(ABC):
    """
    Interface to represent a UseCase.

    All "use cases" classes must implements this interface with the following methods:
    * execute()

    This interface implements the 'Command' Design Pattern.
    """

    @abstractmethod
    def execute(self):
        """
        Abstract Method to execute the use case.

        This method must be implemented in all interfaces that wants to be an "use case".
        Also, this method defines that the class will behave as the 'Command' Design Pattern.
        """
