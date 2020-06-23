from pathlib import Path

from pydantic import BaseSettings

BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    BOT_TOKEN: str
    BASE_DIR: Path = BASE_DIR
    DB_PATH: str = f"sqlite://{(BASE_DIR / 'knowledge_base.db').resolve()}"

    class Config:
        env_file = BASE_DIR / ".env"


settings = Settings()