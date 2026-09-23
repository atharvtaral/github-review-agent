"""
End-to-End Review Pipeline Integration.
Orchestrates fetching PR data, running analyzers, prompting models, and posting back to GitHub.
Defined in Section 17 of the architecture plan.
"""

from typing import Dict, Any, Optional
from github.api_client.github_client import GitHubClient
from github.review_client.review_client import ReviewClient
from agent.context_build.context_builder import ContextBuilder
from agent.router.model_router import ModelRouter
from agent.reviewers.review_engine import ReviewEngine
from analyzers.phpcs.phpcs_runner import PHPCSAnalyzer
from analyzers.phpstan.phpstan_runner import PHPStanAnalyzer
from analyzers.security.security_runner import SecurityAnalyzer
from analyzers.tests.test_runner import PHPUnitRunner

class ReviewPipeline:
    def __init__(self, github_token: Optional[str] = None):
        self.github_client = GitHubClient(token=github_token)
        self.review_client = ReviewClient(token=github_token)
        self.context_builder = ContextBuilder()
        self.router = ModelRouter()
        self.review_engine = ReviewEngine(router=self.router)
        
        # Analyzers
        self.phpcs = PHPCSAnalyzer()
        self.phpstan = PHPStanAnalyzer()
        self.security = SecurityAnalyzer()
        self.tests = PHPUnitRunner()

    def process_pull_request(self, owner: str, repo: str, pull_number: int) -> Dict[str, Any]:
        """
        Executes the end-to-end review flow.
        """
        # 1. Fetch PR details & code diff from GitHub
        pr_details = self.github_client.get_pull_request(owner, repo, pull_number)
        code_diff = self.github_client.get_pull_request_diff(owner, repo, pull_number)
        changed_files = self.github_client.get_changed_files(owner, repo, pull_number)

        # 2. Extract Ticket info (from PR body/title)
        ticket_data = {
            "title": pr_details.get("title", f"PR #{pull_number}"),
            "description": pr_details.get("body", "No description provided.")
        }

        # 3. Run Deterministic Analyzers on changed files
        analyzer_results = {
            "phpcs": [],
            "phpstan": [],
            "security_scan": self.security.run(),
            "phpunit": self.tests.run()
        }
        for file in changed_files:
            analyzer_results["phpcs"].extend(self.phpcs.run(file))
            analyzer_results["phpstan"].extend(self.phpstan.run(file))

        # 4. Run AI Review Engine
        review_result = self.review_engine.run_full_review(
            ticket_data=ticket_data,
            pr_data={
                "title": pr_details.get("title", ""),
                "description": pr_details.get("body", ""),
                "source_branch": pr_details.get("head", {}).get("ref", ""),
                "target_branch": pr_details.get("base", {}).get("ref", ""),
                "changed_files": changed_files
            },
            code_diff=code_diff,
            analyzer_results=analyzer_results
        )

        # 5. Format Markdown comment
        markdown_comment = self.review_client.format_review_markdown(review_result)

        # 6. Post comment back to GitHub PR
        posted = self.review_client.post_pr_comment(owner, repo, pull_number, markdown_comment)

        return {
            "review_result": review_result,
            "markdown": markdown_comment,
            "posted_to_github": posted
        }