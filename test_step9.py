import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from github.review_client.review_client import ReviewClient

    client = ReviewClient()
    
    # Mock Review Result
    mock_result = {
        "decision": "ISSUES",
        "summary": "Payment Service needs retry limits.",
        "blocking_issues": [
            {
                "file": "PaymentService.php",
                "line": 84,
                "problem": "Infinite loop risk in payment retry.",
                "suggestion": "Add max_retries limit = 3"
            }
        ]
    }
    
    markdown_output = client.format_review_markdown(mock_result)
    print("SUCCESS: ReviewClient formatted Markdown output successfully!\n")
    print("Generated Markdown Preview:\n" + "="*40)
    print(markdown_output)
    print("="*40)
except Exception as e:
    print(f"ERROR: {e}")