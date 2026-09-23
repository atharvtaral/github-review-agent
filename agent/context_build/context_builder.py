"""
Context Builder module.
Prepares LLM-ready structured context from raw PR data, tickets, and static analysis outputs.
Defined in Section 5 of the architecture plan.
"""

from typing import Dict, Any, List, Optional

class ContextBuilder:
    def __init__(self):
        pass

    def build_llm_context(
        self,
        ticket_data: Dict[str, Any],
        pr_data: Dict[str, Any],
        code_diff: str,
        analyzer_results: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Extracts and filters relevant PR & ticket context for the LLM pipeline.
        """
        analyzer_results = analyzer_results or {}

        context = {
            "ticket": {
                "title": ticket_data.get("title", "N/A"),
                "description": ticket_data.get("description", "N/A"),
                "acceptance_criteria": ticket_data.get("acceptance_criteria", [])
            },
            "pull_request": {
                "title": pr_data.get("title", "N/A"),
                "description": pr_data.get("description", "N/A"),
                "source_branch": pr_data.get("source_branch", "N/A"),
                "target_branch": pr_data.get("target_branch", "N/A"),
                "changed_files": pr_data.get("changed_files", [])
            },
            "code_diff": code_diff,
            "quality_tool_results": {
                "phpcs": analyzer_results.get("phpcs", []),
                "phpstan": analyzer_results.get("phpstan", []),
                "phpunit": analyzer_results.get("phpunit", []),
                "security_scan": analyzer_results.get("security_scan", [])
            }
        }
        return context

    def format_as_prompt(self, context: Dict[str, Any]) -> str:
        """
        Formats the extracted context into a clean text prompt for the model.
        """
        formatted_prompt = f"""
=== TICKET DETAILS ===
Title: {context['ticket']['title']}
Description: {context['ticket']['description']}
Acceptance Criteria: {context['ticket']['acceptance_criteria']}

=== PULL REQUEST DETAILS ===
Title: {context['pull_request']['title']}
Description: {context['pull_request']['description']}
Changed Files: {', '.join(context['pull_request']['changed_files'])}

=== CODE DIFF ===
{context['code_diff']}

=== AUTOMATED ANALYSIS RESULTS ===
PHPCS Violations: {context['quality_tool_results']['phpcs']}
PHPStan Errors: {context['quality_tool_results']['phpstan']}
Test Results: {context['quality_tool_results']['phpunit']}
Security Scanning: {context['quality_tool_results']['security_scan']}
        """
        return formatted_prompt.strip()