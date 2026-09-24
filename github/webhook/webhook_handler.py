# # """
# # GitHub Webhook Handler Endpoint.
# # Receives incoming webhook events from GitHub and triggers the AI Review Pipeline.
# # Defined in Section 4 of the architecture plan.
# # """

# # from fastapi import FastAPI, Request, HTTPException, BackgroundTasks
# # from typing import Dict, Any
# # from agent.reviewers.review_engine import ReviewEngine

# # app = FastAPI(title="GitHub AI PR Review Agent")
# # review_engine = ReviewEngine()

# # def process_pr_event(payload: Dict[str, Any]):
# #     """
# #     Background task to process the incoming PR event.
# #     """
# #     action = payload.get("action")
# #     print(f"[LOG] Processing PR Action: {action}")

# #     # Extract basic info from Webhook payload
# #     pr_info = payload.get("pull_request", {})
# #     ticket_data = {
# #         "title": pr_info.get("title", "No Ticket Title"),
# #         "description": pr_info.get("body", "No Description")
# #     }
# #     pr_data = {
# #         "title": pr_info.get("title", ""),
# #         "description": pr_info.get("body", ""),
# #         "source_branch": pr_info.get("head", {}).get("ref", ""),
# #         "target_branch": pr_info.get("base", {}).get("ref", ""),
# #         "changed_files": []
# #     }
# #     code_diff = "Sample diff for event processing"

# #     # Run AI Review Pipeline
# #     review_result = review_engine.run_full_review(
# #         ticket_data=ticket_data,
# #         pr_data=pr_data,
# #         code_diff=code_diff
# #     )
# #     print(f"[LOG] Review Completed with Decision: {review_result.get('decision')}")


# # @app.post("/webhook/github")
# # async def github_webhook(request: Request, background_tasks: BackgroundTasks):
# #     """
# #     Endpoint to listen for GitHub Webhooks.
# #     """
# #     event_type = request.headers.get("X-GitHub-Event")
# #     if not event_type:
# #         raise HTTPException(status_code=400, detail="Missing X-GitHub-Event header")

# #     payload = await request.json()

# #     # Process pull_request events
# #     if event_type == "pull_request":
# #         action = payload.get("action")
# #         if action in ["opened", "synchronize", "reopened"]:
# #             # Run review in background to quickly respond to GitHub's webhook ping
# #             background_tasks.add_task(process_pr_event, payload)
# #             return {"status": "processing", "event": event_type, "action": action}

# #     return {"status": "ignored", "event": event_type}

# import os
# from typing import Dict, Any
# from github.review_client.review_client import ReviewClient

# class WebhookHandler:
#     def __init__(self):
#         self.review_client = ReviewClient()

#     def handle_pr_event(self, payload: Dict[str, Any]) -> Dict[str, Any]:
#         action = payload.get("action")
#         print(f"[LOG] Processing PR Action: {action}")

#         # PR उघडल्यावर किंवा अपडेट झाल्यावरच रिव्ह्यू रन करा
#         if action in ["opened", "synchronize", "reopened"]:
#             pull_request = payload.get("pull_request", {})
#             repository = payload.get("repository", {})
            
#             owner = repository.get("owner", {}).get("login")
#             repo = repository.get("name")
#             pull_number = pull_request.get("number")

#             # 1. Review Pipeline रन करा (Mock/Actual Review)
#             review_result = {
#                 "decision": "PASS",
#                 "summary": "✅ All automated checks and AI reviews passed successfully! Code looks clean."
#             }
#             print(f"[LOG] Review Completed with Decision: {review_result['decision']}")

#             # 2. Markdown तयार करा
#             comment_body = self.review_client.format_review_markdown(review_result)

#             # 3. GitHub PR वर Comment पोस्ट करा (हा कॉल सुटला होता!)
#             print(f"[LOG] Attempting to post comment on PR #{pull_number}...")
#             success = self.review_client.post_pr_comment(owner, repo, pull_number, comment_body)

#             if success:
#                 return {"status": "success", "message": "Comment posted to PR"}
#             else:
#                 return {"status": "error", "message": "Failed to post comment to PR"}

#         return {"status": "ignored", "message": f"Action {action} ignored"}


"""
GitHub Webhook Handler Endpoint & Class.
Receives incoming webhook events from GitHub, runs the AI review engine, 
and posts comments back to the GitHub PR.
"""

# import os
# from typing import Dict, Any
# from fastapi import FastAPI, Request, HTTPException, BackgroundTasks

# # Internal Imports
# from agent.reviewers.review_engine import ReviewEngine
# from github.review_client.review_client import ReviewClient

# app = FastAPI(title="GitHub AI PR Review Agent")

# class WebhookHandler:
#     def __init__(self):
#         self.review_engine = ReviewEngine()
#         self.review_client = ReviewClient()

#     def process_pr_event(self, payload: Dict[str, Any]):
#         """
#         Background task to run full AI review and post comment on GitHub PR.
#         """
#         action = payload.get("action")
#         print(f"[LOG] Processing PR Action: {action}")

#         pr_info = payload.get("pull_request", {})
#         repository = payload.get("repository", {})

#         owner = repository.get("owner", {}).get("login")
#         repo = repository.get("name")
#         pull_number = pr_info.get("number")

#         # 1. Extract data for Review Engine
#         ticket_data = {
#             "title": pr_info.get("title", "No Ticket Title"),
#             "description": pr_info.get("body", "No Description")
#         }
#         pr_data = {
#             "title": pr_info.get("title", ""),
#             "description": pr_info.get("body", ""),
#             "source_branch": pr_info.get("head", {}).get("ref", ""),
#             "target_branch": pr_info.get("base", {}).get("ref", ""),
#             "changed_files": []
#         }
#         code_diff = "Sample diff for event processing"

#         # 2. Run AI Review Pipeline
#         review_result = self.review_engine.run_full_review(
#             ticket_data=ticket_data,
#             pr_data=pr_data,
#             code_diff=code_diff
#         )
#         print(f"[LOG] Review Completed with Decision: {review_result.get('decision')}")

#         # 3. Format Review as Markdown
#         comment_body = self.review_client.format_review_markdown(review_result)

#         # 4. Post Comment to GitHub PR
#         print(f"[LOG] Attempting to post review comment to PR #{pull_number}...")
#         success = self.review_client.post_pr_comment(owner, repo, pull_number, comment_body)

#         if success:
#             print(f"[SUCCESS] Review comment posted to PR #{pull_number} successfully!")
#         else:
#             print(f"[ERROR] Failed to post comment to PR #{pull_number}.")


# # Initialize Handler Object
# handler = WebhookHandler()


# @app.get("/")
# def read_root():
#     return {"message": "GitHub AI PR Review Agent is Running Successfully!"}


# @app.post("/webhook/github")
# async def github_webhook(request: Request, background_tasks: BackgroundTasks):
#     """
#     Endpoint to listen for GitHub Webhooks.
#     """
#     event_type = request.headers.get("X-GitHub-Event")
#     if not event_type:
#         raise HTTPException(status_code=400, detail="Missing X-GitHub-Event header")

#     payload = await request.json()

#     # Process pull_request events
#     if event_type == "pull_request":
#         action = payload.get("action")
#         if action in ["opened", "synchronize", "reopened"]:
#             # Run review and comment posting in background
#             background_tasks.add_task(handler.process_pr_event, payload)
#             return {"status": "processing", "event": event_type, "action": action}

#     return {"status": "ignored", "event": event_type}







# ne code 
"""
GitHub Webhook Handler Endpoint & Class with SAST & Inline Commenting support.
"""

import os
import re
from typing import Dict, Any, List
from fastapi import FastAPI, Request, HTTPException, BackgroundTasks

from agent.reviewers.review_engine import ReviewEngine
from github.review_client.review_client import ReviewClient

app = FastAPI(title="GitHub AI PR Review Agent")

class SecurityScanner:
    """Basic SAST Scanner to detect hardcoded secrets & vulnerabilities."""
    
    SECRET_PATTERNS = [
        (r'(?i)(api_key|apikey|secret|token|password)\s*=\s*["\'][A-Za-z0-9_\-]{8,}["\']', "Hardcoded secret/API key detected! Use environment variables instead."),
        (r'SELECT\s+.*\s+FROM\s+.*\s+WHERE\s+.*%s', "Potential SQL Injection vulnerability detected! Use parameterized queries.")
    ]

    @classmethod
    def scan_diff(cls, diff_text: str) -> List[Dict[str, Any]]:
        findings = []
        lines = diff_text.splitlines()
        current_line_num = 0
        
        for line in lines:
            if line.startswith("@@"):
                # Extract starting line number from diff header e.g. @@ -1,3 +1,5 @@
                match = re.search(r'\+(\d+)', line)
                if match:
                    current_line_num = int(match.group(1)) - 1
                continue
            
            if line.startswith("+") and not line.startswith("+++"):
                current_line_num += 1
                code_content = line[1:]
                for pattern, message in cls.SECRET_PATTERNS:
                    if re.search(pattern, code_content):
                        findings.append({
                            "line": current_line_num,
                            "message": f"⚠️ **Security Warning (SAST):** {message}"
                        })
            elif not line.startswith("-"):
                current_line_num += 1
                
        return findings


class WebhookHandler:
    def __init__(self):
        self.review_engine = ReviewEngine()
        self.review_client = ReviewClient()

    def process_pr_event(self, payload: Dict[str, Any]):
        action = payload.get("action")
        print(f"[LOG] Processing PR Action: {action}")

        pr_info = payload.get("pull_request", {})
        repository = payload.get("repository", {})

        owner = repository.get("owner", {}).get("login")
        repo = repository.get("name")
        pull_number = pr_info.get("number")
        commit_id = pr_info.get("head", {}).get("sha")

        ticket_data = {
            "title": pr_info.get("title", "No Ticket Title"),
            "description": pr_info.get("body", "No Description")
        }
        pr_data = {
            "title": pr_info.get("title", ""),
            "description": pr_info.get("body", ""),
            "source_branch": pr_info.get("head", {}).get("ref", ""),
            "target_branch": pr_info.get("base", {}).get("ref", ""),
            "changed_files": []
        }
        
        # Sample diff simulation (In actual flow, fetch diff via GitHub API)
        code_diff = "@@ -1,3 +1,5 @@\n+api_key = \"ghp_1234567890abcdef1234567890\"\n+print('Hello World')"

        # 1. Run Security / SAST Scanner
        security_issues = SecurityScanner.scan_diff(code_diff)

        # 2. Run AI Review Engine
        review_result = self.review_engine.run_full_review(
            ticket_data=ticket_data,
            pr_data=pr_data,
            code_diff=code_diff
        )
        print(f"[LOG] Review Completed with Decision: {review_result.get('decision')}")

        # 3. Post General Summary Comment on PR
        comment_body = self.review_client.format_review_markdown(review_result)
        if security_issues:
            comment_body += "\n\n### 🛡️ Security Findings\n"
            for issue in security_issues:
                comment_body += f"- Line {issue['line']}: {issue['message']}\n"

        self.review_client.post_pr_comment(owner, repo, pull_number, comment_body)

        # 4. Post Inline Comments for Security Findings
        for issue in security_issues:
            self.review_client.post_inline_comment(
                owner=owner,
                repo=repo,
                pull_number=pull_number,
                commit_id=commit_id,
                path="README.md",  # Target modified file path
                line=issue["line"],
                comment_body=issue["message"]
            )


handler = WebhookHandler()


@app.get("/")
def read_root():
    return {"message": "GitHub AI PR Review Agent is Running Successfully!"}


@app.post("/webhook/github")
async def github_webhook(request: Request, background_tasks: BackgroundTasks):
    event_type = request.headers.get("X-GitHub-Event")
    if not event_type:
        raise HTTPException(status_code=400, detail="Missing X-GitHub-Event header")

    payload = await request.json()

    if event_type == "pull_request":
        action = payload.get("action")
        if action in ["opened", "synchronize", "reopened"]:
            background_tasks.add_task(handler.process_pr_event, payload)
            return {"status": "processing", "event": event_type, "action": action}

    return {"status": "ignored", "event": event_type}