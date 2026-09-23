import sys
import os

from analyzers.phpcs.phpcs_runner import PHPCSAnalyzer
from analyzers.phpstan.phpstan_runner import PHPStanAnalyzer
from analyzers.security.security_runner import SecurityAnalyzer
from analyzers.tests.test_runner import PHPUnitRunner

class CodeQualityAnalyzer:
    def __init__(self):
        self.phpcs = PHPCSAnalyzer()
        self.phpstan = PHPStanAnalyzer()
        self.security = SecurityAnalyzer()
        self.tests = PHPUnitRunner()

    def run_all(self, file_paths: list) -> dict:
        results = {
            "phpcs": [],
            "phpstan": [],
            "security_scan": self.security.run(),
            "phpunit": self.tests.run()
        }
        for file in file_paths:
            results["phpcs"].extend(self.phpcs.run(file))
            results["phpstan"].extend(self.phpstan.run(file))
        return results