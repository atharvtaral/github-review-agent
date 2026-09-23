import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from github.api_client.github_client import GitHubClient

    client = GitHubClient()
    
    # Public Repo वरून पब्लिक PR Fetch करून पाहूया (उदा. octocat/Spoon-Knife)
    pr_data = client.get_pull_request(owner="octocat", repo="Spoon-Knife", pull_number=1)
    
    print("SUCCESS: GitHubClient initialized and API connection tested successfully!")
    if pr_data:
        print(f"Fetched PR Title: {pr_data.get('title')}")
except Exception as e:
    print(f"ERROR: {e}")