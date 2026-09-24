# """
# Model Router for directing review tasks to appropriate LLM models/providers.
# Implements the Multi-Model Architecture defined in Sections 6 & 7.
# """

# from typing import Dict, Any, Optional
# #from models.provider_inter.provider_interface import provider_interface
# from models.provider_inter.provider_interface import LLMProviderInterface
# from models.provider_inter.openai_provider import OpenAIProvider



# class ModelRouter:
#     def __init__(
#         self, 
#         fast_model: Optional[LLMProviderInterface] = None,
#         code_model: Optional[LLMProviderInterface] = None,
#         reasoning_model: Optional[LLMProviderInterface] = None,
#         security_model: Optional[LLMProviderInterface] = None
#     ):
#         """
#         Initialize the router with instances of model providers.
#         Defaults to OpenAI instances with recommended models if none are provided.
#         """
#         self.fast_model = fast_model or OpenAIProvider(model_name="gpt-4o-mini")
#         self.code_model = code_model or OpenAIProvider(model_name="gpt-4o")
#         self.reasoning_model = reasoning_model or OpenAIProvider(model_name="gpt-4o")
#         self.security_model = security_model or OpenAIProvider(model_name="gpt-4o")

#     def run_fast_check(self, prompt: str, system_instruction: Optional[str] = None) -> str:
#         """Model 1: Fast/Classification Model for PR parsing & context summary."""
#         return self.fast_model.generate_review(prompt, system_instruction, temperature=0.1)

#     def run_code_review(self, prompt: str, system_instruction: Optional[str] = None) -> str:
#         """Model 2: Code Review Model for identifying bugs, logic, and edge cases."""
#         return self.code_model.generate_review(prompt, system_instruction, temperature=0.2)

#     def run_reasoning_review(self, prompt: str, system_instruction: Optional[str] = None) -> str:
#         """Model 3: Reasoning/Final Review Model for validating requirements vs diff."""
#         return self.reasoning_model.generate_review(prompt, system_instruction, temperature=0.1)

#     def run_security_review(self, prompt: str, system_instruction: Optional[str] = None) -> str:
#         """Model 4: Security-Focused Model for vulnerability scanning."""
#         return self.security_model.generate_review(prompt, system_instruction, temperature=0.1)




# # groq model setting form here 
# """
# Model Router for directing review tasks to appropriate LLM models/providers.
# Implements the Multi-Model Architecture defined in Sections 6 & 7 using Groq Models.
# """

# from typing import Dict, Any, Optional
# from models.provider_inter.provider_interface import LLMProviderInterface
# from models.provider_inter.openai_provider import OpenAIProvider


# class ModelRouter:
#     def __init__(
#         self, 
#         fast_model: Optional[LLMProviderInterface] = None,
#         code_model: Optional[LLMProviderInterface] = None,
#         reasoning_model: Optional[LLMProviderInterface] = None,
#         security_model: Optional[LLMProviderInterface] = None
#     ):
#         """
#         Initialize the router with instances of model providers.
#         Defaults to Groq Llama 3 models if none are provided.
#         """
#         # Fast classification / summary model (Llama 3.3 70B Versatile or Llama 3.1 8B Instant)
#         self.fast_model = fast_model or OpenAIProvider(model_name="llama-3.1-8b-instant")
#         self.code_model = code_model or OpenAIProvider(model_name="llama-3.3-70b-versatile")
#         self.reasoning_model = reasoning_model or OpenAIProvider(model_name="llama-3.3-70b-versatile")
#         self.security_model = security_model or OpenAIProvider(model_name="llama-3.3-70b-versatile")

#     def run_fast_check(self, prompt: str, system_instruction: Optional[str] = None) -> str:
#         """Model 1: Fast/Classification Model for PR parsing & context summary."""
#         return self.fast_model.generate_review(prompt, system_instruction, temperature=0.1)

#     def run_code_review(self, prompt: str, system_instruction: Optional[str] = None) -> str:
#         """Model 2: Code Review Model for identifying bugs, logic, and edge cases."""
#         return self.code_model.generate_review(prompt, system_instruction, temperature=0.2)

#     def run_reasoning_review(self, prompt: str, system_instruction: Optional[str] = None) -> str:
#         """Model 3: Reasoning/Final Review Model for validating requirements vs diff."""
#         return self.reasoning_model.generate_review(prompt, system_instruction, temperature=0.1)

#     def run_security_review(self, prompt: str, system_instruction: Optional[str] = None) -> str:
#         """Model 4: Security-Focused Model for vulnerability scanning."""
#         return self.security_model.generate_review(prompt, system_instruction, temperature=0.1)











"""
Model Router using Groq Supported Models.
"""

from typing import Dict, Any, Optional
from models.provider_inter.provider_interface import LLMProviderInterface
from models.provider_inter.openai_provider import OpenAIProvider


class ModelRouter:
    def __init__(
        self, 
        fast_model: Optional[LLMProviderInterface] = None,
        code_model: Optional[LLMProviderInterface] = None,
        reasoning_model: Optional[LLMProviderInterface] = None,
        security_model: Optional[LLMProviderInterface] = None
    ):
        # Groq Supported Models
        self.fast_model = fast_model or OpenAIProvider(model_name="llama-3.1-8b-instant")
        self.code_model = code_model or OpenAIProvider(model_name="llama-3.3-70b-versatile")
        self.reasoning_model = reasoning_model or OpenAIProvider(model_name="llama-3.3-70b-versatile")
        self.security_model = security_model or OpenAIProvider(model_name="llama-3.3-70b-versatile")

    def run_fast_check(self, prompt: str, system_instruction: Optional[str] = None) -> str:
        return self.fast_model.generate_review(prompt, system_instruction, temperature=0.1)

    def run_code_review(self, prompt: str, system_instruction: Optional[str] = None) -> str:
        return self.code_model.generate_review(prompt, system_instruction, temperature=0.2)

    def run_reasoning_review(self, prompt: str, system_instruction: Optional[str] = None) -> str:
        return self.reasoning_model.generate_review(prompt, system_instruction, temperature=0.1)

    def run_security_review(self, prompt: str, system_instruction: Optional[str] = None) -> str:
        return self.security_model.generate_review(prompt, system_instruction, temperature=0.1)