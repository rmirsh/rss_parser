from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):

    RSS_URL: str = Field(env='RSS_URL')
    TIME_SLEEP: int = Field(env='TIME_SLEEP')
    LOG_FILE: Path = Field(env='LOG_FILE')
    JSON_FILE: Path = Field(env='JSON_FILE')

    model_config = SettingsConfigDict(
            env_file='.env',
            env_file_encoding='utf-8'            
            )


settings = Settings()
