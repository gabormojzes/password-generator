import secrets
from password_generator.config import Config
from password_generator.password import Password
from typing import Self


class Generator:
    _MIN_PASSWORD_LENGTH: int = 1

    def __init__(self: Self, config=None) -> None:
        """
        Initialize the Generator with an optional configuration dictionary.

        Args:
            config (dict[str, any], optional): A dictionary specifying the password generation configuration.
                If not provided, the default configuration will be used.

        The configuration dictionary can include the following keys:
        - 'length': The length of the generated password (default is 8).
        - 'character_sets': A dictionary containing character sets to use for password generation.
          Keys are set identifiers, and values are strings containing characters in the set.
          Example: {'lowercase_letters': 'abcdefghijklmnopqrstuvwxyz', 'uppercase_letters': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}

        Note:
            If 'character_sets' is not provided, default sets will be used as specified in the Config module.
        """
        if config is None:
            config = {}
        self._config: dict[str, any] = config

    def generate(self: Self) -> Password:
        """
        Generate a password based on the provided configuration.

        Returns:
            Password: An object encapsulating the generated password.

        Raises:
            ValueError: If the provided length is less than 1 character
            or if the specified character set is insufficient.
        """
        default_config: dict[str, any] = Config.load()

        length: int = self._config.get('length', default_config.get('length'))
        character_sets: dict[str] = self._config.get('character_sets', default_config.get('character_sets'))

        if length < self._MIN_PASSWORD_LENGTH:
            raise ValueError(f"Password must be at least {self._MIN_PASSWORD_LENGTH} character long.")

        if length < len(character_sets):
            raise ValueError('Password length is insufficient to cover all specified character sets.')

        characters: str = self._get_characters(character_sets)

        while True:
            password: list[str] = self._do_generate(characters, length)
            if self._is_valid(password, character_sets):
                break

        return Password(''.join(password))

    @staticmethod
    def _do_generate(characters: str, length: int) -> list[str]:
        """
        Generate a password based on the configurations.

        Args:
            characters (str): A string containing characters from which to generate the password.
            length (int): Length of the password to be generated.

        Returns:
            list[str]: A list containing a password based on the provided configurations.
        """
        return [secrets.choice(characters) for _ in range(length)]

    @staticmethod
    def _is_valid(password: list[str], character_sets: dict[str]) -> bool:
        """
        Check if the generated password meets the specified requirements.

        Args:
            password (list[str]): The generated password to be validated.
            character_sets (dict[str]): A dictionary containing character sets
                against which the password is to be validated. Keys represent
                the names of character sets, and values are strings containing
                characters belonging to each set.

        Returns:
            bool: True if the password is valid, False otherwise.
        """
        # Check if at least one character from each character set is present in the password
        return all(
            any(character in password for character in characters)
            for characters in character_sets.values()
        )

    @staticmethod
    def _get_characters(character_sets: dict[str]) -> str:
        """
        Get the characters based on the configuration.

        Args:
            character_sets (dict[str]): A dictionary containing sets of characters.

        Returns:
            str: The characters to use for password generation.

        Raises:
            ValueError: If no characters were provided.
        """
        characters: str = ''.join(character_sets.values())

        if not characters:
            raise ValueError('Password generation failed: No characters were provided.')

        return characters
