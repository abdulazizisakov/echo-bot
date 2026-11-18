import os

from dotenv import load_dotenv


class Settings:
    token = os.getenv('TOKEN')

    def __init__(self, path: str = '.env'):
        self.__load_env(path)

    def __load_env(self, path: str) -> None:
        load_dotenv(path)


settings = Settings()
