import math


class EntropyCalculator:
    _LOWERCASE_LETTERS = 26
    _UPPERCASE_LETTERS = 26
    _DIGITS = 10
    _SPECIAL_CHARACTERS = 32

    @classmethod
    def calculate(cls, password: str) -> float:
        """
        Calculate the entropy of a password based on its character sets and length.

        Args:
            password (str): The input password.

        Returns:
            float: The calculated entropy of the password, truncated to two decimal places.
        """
        character_sets: list[int] = [
            cls._LOWERCASE_LETTERS if any(character.islower() for character in password) else 0,
            cls._UPPERCASE_LETTERS if any(character.isupper() for character in password) else 0,
            cls._DIGITS if any(character.isdigit() for character in password) else 0,
            cls._SPECIAL_CHARACTERS if any(not character.isalnum() for character in password) else 0
        ]

        entropy: float = math.log2(sum(character_sets) ** len(password))
        entropy: float = EntropyCalculator._truncate_to_two_decimals(entropy)
        return entropy

    @staticmethod
    def _truncate_to_two_decimals(value: float) -> float:
        """
        Truncate a floating-point value to two decimal places.

        Args:
            value (float): The input floating-point value.

        Returns:
            float: The truncated value.
        """
        return math.trunc(value * 100) / 100
