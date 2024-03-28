from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):

    RSS_URL: str = Field(env="RSS_URL")
    TIME_SLEEP: int = Field(env="TIME_SLEEP")
    LOG_FILE: str = Field(env="LOG_FILE")
    JSON_FILE: str = Field(env="JSON_FILE")
    SHOW_STATISTICS: bool = Field(env="SHOW_STATISTICS")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
