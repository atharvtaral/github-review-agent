import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from github.webhook.webhook_handler import app
    print("SUCCESS: FastAPI Webhook Handler initialized successfully!")
except Exception as e:
    print(f"ERROR: {e}")