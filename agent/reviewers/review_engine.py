"""
Review Engine module.
Executes the multi-model review pipeline and generates structured JSON output & final decision.
Defined in Sections 9 & 10 of the architecture plan.
"""

import json
from typing import Dict, Any, Optional
from agent.router.model_router import ModelRouter
from agent.context_build.context_builder import ContextBuilder

SYSTEM_REVIEW_PROMPT = """
You are an expert AI Code Reviewer.
Analyze the provided Ticket, Pull Request, Diff, and Automated Tool Results.

You MUST respond strictly with a valid JSON object using the following structure:
{
    "decision": "PASS" or "ISSUES",
    "summary": "High-level review summary",
    "blocking_issues": [
        {
            "file": "file_name.php",
            "line": 84,
            "severity": "high",
            "problem": "Brief description of problem",
            "reason": "Why this is a problem",
            "suggestion": "How to fix it"
        }
    ],
    "non_blocking_issues": []
}
Do not include markdown formatting or extra text outside the JSON object.
"""

class ReviewEngine:
    def __init__(self, router: Optional[ModelRouter] = None):
        self.router = router or ModelRouter()
        self.context_builder = ContextBuilder()

    def run_full_review(
        self,
        ticket_data: Dict[str, Any],
        pr_data: Dict[str, Any],
        code_diff: str,
        analyzer_results: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Runs the context builder, queries LLMs, and formats the decision output.
        """
        # 1. Build Context
        context = self.context_builder.build_llm_context(
            ticket_data, pr_data, code_diff, analyzer_results
        )
        formatted_prompt = self.context_builder.format_as_prompt(context)

        # 2. Call Reasoning Model for Structured Review
        raw_response = self.router.run_reasoning_review(
            prompt=formatted_prompt,
            system_instruction=SYSTEM_REVIEW_PROMPT
        )

        # 3. Parse JSON Response safely
        try:
            # Clean potential markdown wrapping (e.g. ```json ... ```)
            clean_json = raw_response.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
            review_result = json.loads(clean_json)
        except Exception:
            review_result = {
                "decision": "ISSUES",
                "summary": "AI response parsing failed.",
                "blocking_issues": [{
                    "file": "N/A",
                    "line": 0,
                    "severity": "high",
                    "problem": "Invalid JSON returned by AI model",
                    "reason": raw_response,
                    "suggestion": "Ensure model adheres to strict JSON format"
                }],
                "non_blocking_issues": []
            }

        return review_result