"""
PHPCS Runner Module.
"""

import json
import subprocess
from typing import List, Dict, Any

class PHPCSAnalyzer:
    def __init__(self, standard: str = "Drupal"):
        self.standard = standard

    def run(self, file_path: str) -> List[Dict[str, Any]]:
        try:
            cmd = ["phpcs", f"--standard={self.standard}", "--report=json", file_path]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.stdout:
                data = json.loads(result.stdout)
                return data.get("files", {}).get(file_path, {}).get("messages", [])
        except Exception:
            pass
        return []