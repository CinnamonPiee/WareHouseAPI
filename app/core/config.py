from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings


if not find_dotenv():
    exit("Environment variables are not loaded because the file is missing .env")
else:
    load_dotenv()


class Settings(BaseSettings):
    api_prefix: str = "/api"

    db_host: str
    db_port: str
    db_user: str
    db_pass: str
    db_name: str

    db_echo: bool = False

    @property
    def db_url(self):
        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"

    class Config:
        env_file = ".env"



settings = Settings()