from pathlib import Path

from pydantic import BaseSettings

BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    BOT_TOKEN: str
    BASE_DIR: Path = BASE_DIR
    DB_PATH: str = "sqlite:///knowledge_base.db"

    class Config:
        env_file = BASE_DIR / ".env"


settings = Settings()
