import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from models.provider_inter.provider_interface import LLMProviderInterface
    from models.provider_inter.openai_provider import OpenAIProvider
    print("SUCCESS: Circular import completely resolved and modules loaded successfully!")
except Exception as e:
    print(f"ERROR: {e}")