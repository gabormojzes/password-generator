import secrets
import random
from password_generator.config import Config
from password_generator.password import Password
from typing import Self


class Generator:
    _MIN_PASSWORD_LENGTH: int = 4
    _CHARACTER_TYPES: list[str] = ['lowercase_letters', 'uppercase_letters', 'digits', 'special_characters']

    def __init__(self: Self, config: dict[str, any]) -> None:
        """
        Initialise the Generator with a configuration dictionary.

        Args:
            config (dict[str, any]): A dictionary specifying the password generation configuration.

        The configuration dictionary can include the following keys:
        - 'length': The length of the generated password (default is 8).
        - 'lowercase_letters': Include lowercase letters in the password.
        - 'uppercase_letters': Include uppercase letters in the password.
        - 'digits': Include digits in the password.
        - 'special_characters': Include special characters in the password.
        """
        self._config: dict[str, any] = config

    def generate(self: Self) -> Password:
        """
        Generate a password based on the provided configuration.

        Returns:
            Password: A Password object containing the generated password.

        Raises:
            ValueError: If the provided length is less than the _MIN_PASSWORD_LENGTH.
        """
        length: int = self._config.get('length', Config.get().get('length'))
        if length < self._MIN_PASSWORD_LENGTH:
            raise ValueError(f'Password must be at least {self._MIN_PASSWORD_LENGTH} characters long.')

        password: list[str] = self._generate_partial_password()
        character_set: str = self._get_character_set()
        password += [secrets.choice(character_set) for _ in range(length - len(password))]

        random.shuffle(password)

        return Password(''.join(password))

    def _generate_partial_password(self: Self) -> list[str]:
        """
        Generate a partial password based on the configurations.

        Returns:
            list: A list containing a partial password based on the provided configurations.
        """
        config: dict[str, any] = self._config
        partial_password: list[str] = [
            secrets.choice(config.get(character_type))
            for character_type in self._CHARACTER_TYPES
            if config.get(character_type)
        ]
        return partial_password

    def _get_character_set(self: Self) -> str:
        """
        Get the character set based on the configuration.

        Returns:
            str: The character set to use for password generation.

        Raises:
            ValueError: If no characters were provided.

        This method constructs a character set based on the configuration settings.
        The character set can include lowercase letters, uppercase letters, digits, and special characters
        as specified in the configuration.
        """
        config: dict[str, any] = self._config
        characters: str = ''.join(config.get(key) for key in self._CHARACTER_TYPES if config.get(key))

        if not characters:
            raise ValueError('Password generation failed: No characters were provided.')

        return characters
