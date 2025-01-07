from pydantic import SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Application metadata
    PROJECT_NAME: str = 'FastAPI Template'
    PROJECT_VERSION: str = '1.0.0'

    # Database configuration
    DATABASE_URL: str

    # Authentication configuration
    SECRET_KEY: SecretStr
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # S3 Configuration
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: SecretStr
    AWS_STORAGE_BUCKET_NAME: str
    AWS_S3_REGION: str = 'eu-north-1'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
