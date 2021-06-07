from typing import List

from pydantic import BaseSettings


class Base(BaseSettings):
    class Config:
        env_file = ".env"


class TitleSettings(Base):
    title: str = "Hello, World!"
    number: int

    class Config:
        env_prefix = "app_"


class LogSettings(Base):
    streams: List[str]

    class Config:
        env_prefix = "app_log_"


class Settings(Base):
    title: TitleSettings = TitleSettings()
    log: LogSettings = LogSettings()


if __name__ == "__main__":
    s = Settings()
    print(s)
