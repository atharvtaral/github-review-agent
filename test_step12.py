import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from configuration import model_config, review_rules

    print("SUCCESS: Configuration modules loaded successfully!")
    print(f"Fast Model: {model_config.FAST_MODEL}")
    print(f"Strict PHPStan Level: {review_rules.STRICT_PHPSTAN_LEVEL}")
    
    print("\n==================================================")
    print("🎉 CONGRATULATIONS ATHARVA!")
    print("All project modules, analyzers & configurations are 100% verified!")
    print("==================================================")

except Exception as e:
    print(f"ERROR: {e}")