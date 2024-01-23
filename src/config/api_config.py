from pydantic import BaseSettings, Field

# env_filename = os.getenv("ENV_FILENAME", ".env")


class ApiConfig(BaseSettings):
    """
    All API Settings are here
    """

    APP_NAME: str = "Online Auctions API"
    DEBUG: bool = Field(env="DEBUG", default=True)
    DATABASE_ECHO: bool = Field(env="DATABASE_ECHO", default=True)
    DATABASE_URL: str = Field(
        env="DATABASE_URL",
        default="postgresql://postgres:password@db:5432/postgres",
    )
    LOGGER_NAME = "api"


# SECRET_KEY = config("SECRET_KEY", cast=Secret, default="secret")
# ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=CommaSeparatedStrings, default="*")
