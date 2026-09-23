"""
Model Configuration Module.
Loads environment variables, API keys, and model parameters.
"""

import os
from dotenv import load_dotenv

load_dotenv()

class ModelConfig:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    GITHUB_TOKEN: str = os.getenv("GITHUB_TOKEN", "")
    
    FAST_MODEL: str = os.getenv("DEFAULT_FAST_MODEL", "gpt-4o-mini")
    CODE_MODEL: str = os.getenv("DEFAULT_CODE_MODEL", "gpt-4o")
    REASONING_MODEL: str = os.getenv("DEFAULT_REASONING_MODEL", "gpt-4o")
    SECURITY_MODEL: str = os.getenv("DEFAULT_SECURITY_MODEL", "gpt-4o")

model_config = ModelConfig()