from pathlib import Path

from pydantic import BaseSettings, FilePath

BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    BOT_TOKEN: str
    BASE_DIR: Path = BASE_DIR
    DB_PATH: FilePath = f"{BASE_DIR.resolve()}/knowledge_base.db"
    DB_DSN: str = f"sqlite://{DB_PATH}"

    class Config:
        env_file = BASE_DIR / ".env"


settings = Settings()
