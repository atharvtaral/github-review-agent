import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from agent.router.model_router import ModelRouter
    router = ModelRouter()
    print("SUCCESS: ModelRouter initialized with default OpenAI models successfully!")
except Exception as e:
    print(f"ERROR: {e}")