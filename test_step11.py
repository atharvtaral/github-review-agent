import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from agent.reviewers.review_pipeline import ReviewPipeline

    pipeline = ReviewPipeline()
    print("SUCCESS: Full ReviewPipeline integrated and initialized successfully!")
except Exception as e:
    print(f"ERROR: {e}")