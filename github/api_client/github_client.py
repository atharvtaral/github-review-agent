"""
GitHub API Client module.
Fetches PR details, changed files, and code diffs directly from GitHub via API.
Defined in Section 4 of the architecture plan.
"""

import requests
from typing import Dict, Any, List, Optional

class GitHubClient:
    def __init__(self, token: Optional[str] = None):
        """
        Initialize GitHub Client with optional Personal Access Token or App Token.
        """
        self.token = token
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "GitHub-AI-Review-Agent"
        }
        if self.token:
            self.headers["Authorization"] = f"token {self.token}"

    def get_pull_request(self, owner: str, repo: str, pull_number: int) -> Dict[str, Any]:
        """Fetch PR details from GitHub."""
        url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        return {}

    def get_pull_request_diff(self, owner: str, repo: str, pull_number: int) -> str:
        """Fetch raw code diff for a Pull Request."""
        url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}"
        headers = self.headers.copy()
        headers["Accept"] = "application/vnd.github.v3.diff"
        
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return ""

    def get_changed_files(self, owner: str, repo: str, pull_number: int) -> List[str]:
        """Fetch list of modified file names in a Pull Request."""
        url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/files"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return [file_item["filename"] for file_item in response.json()]
        return []