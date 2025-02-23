"""
Environment variables settings for project.
"""
from pydantic import SecretStr, EmailStr
from pydantic_settings import BaseSettings


class EnvSettings(BaseSettings):
    """Settings class for managing environment variables used in the application."""
    CURRENT_ENV: str
    DB_HOST: str
    DB_USER: str
    DB_PASSWORD: SecretStr
    DB_PORT: int
    DB_NAME: str
    DJANGO_SECRET_KEY: SecretStr
    DJANGO_ALLOWED_HOSTS: str
    EMAIL_HOST_USER: EmailStr
    EMAIL_HOST_PASSWORD: SecretStr
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        allow_extra = True

# Instantiate the settings
env_settings = EnvSettings()
