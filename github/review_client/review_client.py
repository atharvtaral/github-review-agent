# """
# GitHub Review Client module.
# Posts AI Code Review summary and comments back to GitHub Pull Requests.
# Defined in Section 15 of the architecture plan.
# """

# import requests
# from typing import Dict, Any, Optional

# class ReviewClient:
#     def __init__(self, token: Optional[str] = None):
#         self.token = token
#         self.headers = {
#             "Accept": "application/vnd.github.v3+json",
#             "User-Agent": "GitHub-AI-Review-Agent"
#         }
#         if self.token:
#             self.headers["Authorization"] = f"token {self.token}"

#     def format_review_markdown(self, review_result: Dict[str, Any]) -> str:
#         """
#         Formats the review dictionary into Markdown suitable for GitHub PR comments.
#         """
#         decision = review_result.get("decision", "ISSUES")
#         summary = review_result.get("summary", "No summary provided.")
#         blocking = review_result.get("blocking_issues", [])
#         non_blocking = review_result.get("non_blocking_issues", [])

#         if decision == "PASS":
#             markdown = "## 🤖 AI Code Review: PASS ✅\n\n"
#             markdown += f"**Summary:** {summary}\n\n"
#             markdown += "✨ *No blocking issues found. Code is ready to merge!*"
#         else:
#             markdown = "## 🤖 AI Code Review: ISSUES FOUND ❌\n\n"
#             markdown += f"**Summary:** {summary}\n\n"
            
#             if blocking:
#                 markdown += "### 🚨 Blocking Issues:\n"
#                 for idx, issue in enumerate(blocking, 1):
#                     file_name = issue.get("file", "N/A")
#                     line = issue.get("line", "N/A")
#                     problem = issue.get("problem", "N/A")
#                     suggestion = issue.get("suggestion", "N/A")
#                     markdown += f"{idx}. **`{file_name}` (Line {line})**\n"
#                     markdown += f"   - **Problem:** {problem}\n"
#                     markdown += f"   - **Suggestion:** {suggestion}\n\n"

#             if non_blocking:
#                 markdown += "### ⚠️ Non-Blocking Suggestions:\n"
#                 for idx, issue in enumerate(non_blocking, 1):
#                     markdown += f"{idx}. {issue.get('problem')} (`{issue.get('file')}`)\n"

#         return markdown

#     def post_pr_comment(self, owner: str, repo: str, pull_number: int, comment_body: str) -> bool:
#         """
#         Posts a comment on the specified GitHub Pull Request.
#         """
#         url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pull_number}/comments"
        
#         if not self.token:
#             print("[LOG] GitHub Token missing. Skipping live PR comment post.")
#             return False

#         payload = {"body": comment_body}
#         response = requests.post(url, json=payload, headers=self.headers)
#         return response.status_code == 201


import os
import requests
from typing import Dict, Any

class ReviewClient:
    def __init__(self, token: str = None):
        self.token = token or os.getenv("GITHUB_TOKEN", "")

    def format_review_markdown(self, review_result: Dict[str, Any]) -> str:
        decision = review_result.get("decision", "PASS")
        summary = review_result.get("summary", "No issues found.")
        
        md = f"## 🤖 GitHub AI PR Review Agent\n\n"
        md += f"**Decision:** `{decision}`\n\n"
        md += f"### Summary\n{summary}\n\n"
        return md

    def post_pr_comment(self, owner: str, repo: str, pull_number: int, comment_body: str) -> bool:
        if not self.token:
            print("[ERROR] GITHUB_TOKEN is missing in .env file!")
            return False

        url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pull_number}/comments"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
        data = {"body": comment_body}
        
        response = requests.post(url, json=data, headers=headers)
        
        if response.status_code == 201:
            print("[SUCCESS] Review comment posted to GitHub PR successfully!")
            return True
        else:
            print(f"[ERROR] GitHub API Failed ({response.status_code}): {response.text}")
            return False