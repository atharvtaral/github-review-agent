import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from agent.reviewers.review_engine import ReviewEngine

    engine = ReviewEngine()
    print("SUCCESS: ReviewEngine imported and initialized successfully!")
except Exception as e:
    print(f"ERROR: {e}")