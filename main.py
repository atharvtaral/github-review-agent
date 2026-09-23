"""
Main application entry point.
Runs the FastAPI server using Uvicorn.
"""

import sys
import os
import uvicorn

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from github.webhook.webhook_handler import app


@app.get("/")
def home():
    return {"message": "GitHub AI PR Review Agent is Running Successfully!"}

if __name__ == "__main__":
    print("Starting GitHub AI PR Review Agent Webhook Server...")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)