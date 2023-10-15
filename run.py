from password_generator.config import Config
from password_generator.generator import Generator
from password_generator.password import Password

password: Password = Generator(Config.get()).generate()
print(password)
