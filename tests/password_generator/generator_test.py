import unittest
from typing import Self

from password_generator.config import Config
from password_generator.generator import Generator
from password_generator.password import Password


class GeneratorTest(unittest.TestCase):
    def setUp(self: Self) -> None:
        self._config: dict[str, any] = Config.get()
        self._generator: Generator = Generator(self._config)

    def test_generated_password_has_correct_length(self: Self) -> None:
        password: Password = self._generator.generate()
        self.assertEqual(len(password.to_string()), self._config.get('length'))

    def test_generated_password_contains_lowercase_characters(self: Self) -> None:
        password: Password = self._generator.generate()
        self.assertTrue(any(character.islower() for character in password.to_string()))

    def test_generated_password_contains_uppercase_characters(self: Self) -> None:
        password: Password = self._generator.generate()
        self.assertTrue(any(character.isupper() for character in password.to_string()))

    def test_generated_password_contains_digits(self: Self) -> None:
        password: Password = self._generator.generate()
        self.assertTrue(any(character.isdigit() for character in password.to_string()))

    def test_generated_password_contains_special_characters(self: Self) -> None:
        password: Password = self._generator.generate()
        self.assertTrue(
            any(self._config.get('special_characters').find(character) != -1 for character in password.to_string()))

    def test_generate_password_with_invalid_length_raises_value_error(self: Self) -> None:
        self._config['length']: int = 0

        with self.assertRaises(ValueError):
            self._generator.generate()
