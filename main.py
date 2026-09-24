# """
# Main application entry point.
# Runs the FastAPI server using Uvicorn.
# """

# import sys
# import os
# import uvicorn

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# from github.webhook.webhook_handler import app


# @app.get("/")
# def home():
#     return {"message": "GitHub AI PR Review Agent is Running Successfully!"}

# if __name__ == "__main__":
#     print("Starting GitHub AI PR Review Agent Webhook Server...")
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)










"""
Main application entry point.
Runs the FastAPI server using Uvicorn.
"""

import sys
import os

import importlib


def load_dotenv(path=".env"):
    """Load simple KEY=VALUE entries without requiring python-dotenv."""
    if not os.path.isfile(path):
        return

    with open(path, encoding="utf-8") as env_file:
        for line in env_file:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip("\"'"))

# Load environment variables from .env file before importing handler
load_dotenv()

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from github.webhook.webhook_handler import app


@app.get("/")
def home():
    return {"message": "GitHub AI PR Review Agent is Running Successfully!"}


if __name__ == "__main__":
    print("Starting GitHub AI PR Review Agent Webhook Server...")
    uvicorn = importlib.import_module("uvicorn")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)