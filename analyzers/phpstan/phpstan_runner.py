"""
PHPStan Runner Module.
"""

import json
import subprocess
from typing import List, Dict, Any

class PHPStanAnalyzer:
    def __init__(self, level: int = 5):
        self.level = level

    def run(self, file_path: str) -> List[Dict[str, Any]]:
        try:
            cmd = ["phpstan", "analyze", f"--level={self.level}", "--error-format=json", file_path]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.stdout:
                data = json.loads(result.stdout)
                return data.get("files", {}).get(file_path, {}).get("messages", [])
        except Exception:
            pass
        return []