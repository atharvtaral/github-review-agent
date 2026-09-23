"""
Review Rules & Thresholds Module.
Defines review severity rules, strictness, and pass/fail thresholds.
"""

from typing import Dict, Any

class ReviewRules:
    SEVERITY_LEVELS = ["low", "medium", "high", "critical"]
    
    # Failing thresholds
    FAIL_ON_BLOCKING_ISSUES: bool = True
    MAX_ALLOWED_NON_BLOCKING: int = 5
    
    # PHP / Drupal specific standards enable/disable flags
    STRICT_PHPCS_CHECK: bool = True
    STRICT_PHPSTAN_LEVEL: int = 5

review_rules = ReviewRules()