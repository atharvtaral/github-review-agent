import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from agent.context_build.context_builder import ContextBuilder

    builder = ContextBuilder()
    
    # Mock Data for Testing
    mock_ticket = {"title": "Fix Payment Retry", "description": "Limit retries to max 3 times."}
    mock_pr = {"title": "Payment fix implementation", "description": "Added retry counter", "changed_files": ["PaymentService.php"]}
    mock_diff = "+ if ($retryCount > 3) return false;"
    
    ctx = builder.build_llm_context(mock_ticket, mock_pr, mock_diff)
    prompt = builder.format_as_prompt(ctx)
    
    print("SUCCESS: ContextBuilder built prompt successfully!")
    print("\nGenerated Prompt Preview:\n" + "-"*30)
    print(prompt[:250] + "...\n" + "-"*30)
except Exception as e:
    print(f"ERROR: {e}")