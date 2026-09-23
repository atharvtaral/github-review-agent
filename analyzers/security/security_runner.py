"""
Security Scanner Module.
"""

import subprocess
import json
from typing import List, Dict, Any

class SecurityAnalyzer:
    def __init__(self):
        pass

    def run(self, project_path: str = ".") -> List[Dict[str, Any]]:
        security_issues = []
        try:
            cmd = ["composer", "audit", "--format=json"]
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=project_path)
            if result.stdout:
                data = json.loads(result.stdout)
                advisories = data.get("advisories", {})
                for pkg, issues in advisories.items():
                    for issue in issues:
                        security_issues.append({
                            "package": pkg,
                            "title": issue.get("title", "Security Vulnerability"),
                            "cve": issue.get("cve", "N/A"),
                            "severity": "high"
                        })
        except Exception:
            pass
        return security_issues