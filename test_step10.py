import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from analyzers.phpcs.phpcs_runner import PHPCSAnalyzer
    from analyzers.phpstan.phpstan_runner import PHPStanAnalyzer
    from analyzers.security.security_runner import SecurityAnalyzer
    from analyzers.tests.test_runner import PHPUnitRunner

    a1 = PHPCSAnalyzer()
    a2 = PHPStanAnalyzer()
    a3 = SecurityAnalyzer()
    a4 = PHPUnitRunner()

    print("SUCCESS: All 4 Analyzers (PHPCS, PHPStan, Security, Tests) imported successfully!")
except Exception as e:
    print(f"ERROR: {e}")