from pydantic import BaseSettings, SecretStr
import os


class Settings(BaseSettings):
    API_TOKEN: SecretStr
    webhook: SecretStr
    ip_address: SecretStr

    class Config:
        env_file = f"{os.path.dirname(__file__)}/" + ".env"
        env_file_encoding = 'utf-8'


config = Settings()
