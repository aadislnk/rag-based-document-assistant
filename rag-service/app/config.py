from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[2] / ".env",
        extra="ignore",
    )
    database_url: str = "postgresql://askmydocs:local-development-only@localhost:5432/askmydocs"
    internal_service_key: str = "local-development-only"
    embedding_model_name: str = "sentence-transformers/all-MiniLM-L6-v2"
    rag_min_similarity: float = 0.7
    max_upload_size_mb: int = 25
    max_pdf_pages: int = 200
    llm_api_key: str = ""
    llm_model_name: str = "gpt-4o-mini"
    llm_base_url: str = "https://api.openai.com/v1"


settings = Settings()
