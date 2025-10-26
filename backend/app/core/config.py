import os
from dataclasses import dataclass
from dotenv import load_dotenv


load_dotenv()


@dataclass
class Settings:
    environment: str = os.getenv("ENVIRONMENT", "development")
    db_url: str | None = os.getenv("DATABASE_URL")
    vector_url: str | None = os.getenv("VECTOR_URL")
    hf_token: str | None = os.getenv("HF_TOKEN")
    openrouter_api_key: str | None = os.getenv("OPENROUTER_API_KEY")


settings = Settings()

