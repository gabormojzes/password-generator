from password_generator.entropy_calculator import EntropyCalculator
from typing import Self


class Password:
    def __init__(self: Self, password: str) -> None:
        """
        Constructor for the Password class.

        Args:
            password (str): The password string to be stored.
        """
        self._password: str = password

    def __str__(self: Self) -> str:
        """
        Get a string representation of the Password object, which is the stored password.

        Returns:
            str: The stored password string.
        """
        return self._password

    def to_string(self: Self) -> str:
        """
        Retrieve the stored password.

        Returns:
            str: The stored password string.
        """
        return self._password

    def calculate_entropy(self: Self) -> float:
        """
        Calculate the entropy of a password based on its character sets and length.

        Returns:
            float: The calculated entropy of the password, truncated to two decimal places.
        """
        return EntropyCalculator.calculate(self._password)
