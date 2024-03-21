from password_generator.config import Config
from password_generator.generator import Generator
from password_generator.password import Password

try:
    password: Password = Generator(Config.load()).generate()
    print(password)
except Exception as e:
    print(f"Error: {e}")
