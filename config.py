from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):

    RSS_URL: str = Field(env="RSS_URL")
    INTERVAL: int = Field(env="INTERVAL")
    LOG_FILE: Path = Field(env="LOG_FILE")
    JSON_FILE: Path = Field(env="JSON_FILE")
    SHOW_STATISTICS: bool = Field(env="SHOW_STATISTICS")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
