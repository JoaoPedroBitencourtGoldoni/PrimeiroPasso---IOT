import os
from dataclasses import dataclass
from dotenv import load_dotenv
load_dotenv()
@dataclass(frozen=True)
class Settings:
    provider: str = os.getenv("LLM_PROVIDER", "ollama")
    ollama_url: str = os.getenv("OLLAMA_URL", "http://localhost:11434")
    ollama_model: str = os.getenv("OLLAMA_MODEL", "llama3.2:3b")
    openai_url: str = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    openai_key: str = os.getenv("OPENAI_API_KEY", "")
    internal_key: str = os.getenv("INTERNAL_API_KEY", "")
    timeout: float = float(os.getenv("REQUEST_TIMEOUT", "60"))
settings = Settings()
