import string


class Config:
    @staticmethod
    def load() -> dict[str, any]:
        """
        Retrieve the default configuration parameters for generating passwords.

        Returns:
            dict[str, any]: A dictionary containing various configuration parameters.

        Configuration Parameters:
            - 'length' (int): The length of the generated password (default is 8).
            - 'character_sets' (dict[str]): A dictionary containing character sets for password generation.
                - 'lowercase_letters' (str): String constant containing all lowercase letters from 'a' to 'z'.
                - 'uppercase_letters' (str): String constant containing all uppercase letters from 'A' to 'Z'.
                - 'digits' (str): String constant containing all numerical digits from '0' to '9'.
                - 'special_characters' (str): String constant containing commonly used special characters.
        """
        return {
            'length': 8,
            'character_sets': {
                'lowercase_letters': string.ascii_lowercase,
                'uppercase_letters': string.ascii_uppercase,
                'digits': string.digits,
                'special_characters': string.punctuation
            }
        }
