# Password Generator
A customisable Python package utilised for generating random passwords, featuring an integrated password entropy calculator.

### How to use
After installing the package use following import:
```
from password_generator.config import Config
from password_generator.generator import Generator
from password_generator.password import Password
```

Then use following commands:
```
password: Password = Generator(Config.load()).generate()
print(password)  # The password can be retrieved using the 'password.to_string()' method.
```

Using custom configuration:
```
config: dict[str, any] = {
    'length': 8,  # The length of the generated password (default is 8). Optional.
    'character_sets': {
        'lowercase_letters': 'abcdefghijklmnopqrstuvwxyz',  # Optional
        'uppercase_letters': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',  # Optional
        'digits': '0123456789',  # Optional
        'special_characters': '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'  # Optional
    }
}

password: Password = Generator(config).generate()
print(password)
```
or
```
config: dict[str, any] = Config.load()
config['length']: int = 12

password: Password = Generator(config).generate()
print(password)
```

Calculating password entropy:
```
password: Password = Generator(Config.load()).generate()
print(password.calculate_entropy())
```
