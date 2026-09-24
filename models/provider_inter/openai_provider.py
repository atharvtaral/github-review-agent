# """
# OpenAI Provider Implementation.
# """

# import os
# from dotenv import load_dotenv
# from typing import Optional
# from openai import OpenAI
# from models.provider_inter.provider_interface import LLMProviderInterface

# load_dotenv()

# class OpenAIProvider(LLMProviderInterface):
#     def __init__(self, model_name: str = "gpt-4o-mini", api_key: Optional[str] = None):
#         self.model_name = model_name
#         self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        
#         if not self.api_key:
#             raise ValueError("OPENAI_API_KEY is missing. Set it in .env or as a parameter.")
            
#         self.client = OpenAI(api_key=self.api_key)

#     def generate_review(
#         self, 
#         prompt: str, 
#         system_instruction: Optional[str] = None,
#         temperature: float = 0.2
#     ) -> str:
#         messages = []
        
#         if system_instruction:
#             messages.append({"role": "system", "content": system_instruction})
            
#         messages.append({"role": "user", "content": prompt})
        
#         response = self.client.chat.completions.create(
#             model=self.model_name,
#             messages=messages,
#             temperature=temperature
#         )
        
#         return response.choices[0].message.content




# # Groq Model Provider
# import os
# from groq import Groq

# class OpenAIProvider:
#     """Provider wrapper for Groq LLM inference."""
#     def __init__(self, model_name: str = "llama-3.3-70b-versatile"):
#         self.api_key = os.getenv("GROQ_API_KEY")
#         if not self.api_key:
#             raise ValueError("GROQ_API_KEY is missing. Set it in .env or GitHub Secrets.")
        
#         self.client = Groq(api_key=self.api_key)
#         self.model_name = model_name

#     def generate_review(self, prompt: str) -> str:
#         """Call Groq API to generate PR review summary."""
#         response = self.client.chat.completions.create(
#             model=self.model_name,
#             messages=[
#                 {"role": "system", "content": "You are an expert AI Code Reviewer and Security Auditor."},
#                 {"role": "user", "content": prompt}
#             ],
#             temperature=0.2
#         )
#         return response.choices[0].message.content












# import os
# from groq import Groq
# from typing import Optional

# class OpenAIProvider:
#     """Provider wrapper for Groq LLM inference."""
    
#     def __init__(self, model_name: str = "llama-3.3-70b-versatile"):
#         self.api_key = os.getenv("GROQ_API_KEY")
#         if not self.api_key:
#             raise ValueError("GROQ_API_KEY is missing. Set it in .env or GitHub Secrets.")
        
#         self.client = Groq(api_key=self.api_key)
#         self.model_name = model_name

#     def generate_review(
#         self, 
#         prompt: str, 
#         system_instruction: Optional[str] = None, 
#         temperature: float = 0.2
#     ) -> str:
#         """Call Groq API to generate PR review summary."""
#         messages = []
        
#         if system_instruction:
#             messages.append({"role": "system", "content": system_instruction})
#         else:
#             messages.append({"role": "system", "content": "You are an expert AI Code Reviewer and Security Auditor."})
            
#         messages.append({"role": "user", "content": prompt})

#         response = self.client.chat.completions.create(
#             model=self.model_name,
#             messages=messages,
#             temperature=temperature
#         )
#         return response.choices[0].message.content











# import os
# from google import genai
# from typing import Optional

# class OpenAIProvider:
#     """Provider wrapper for Google Gemini LLM inference."""
    
#     def __init__(self, model_name: str = "gemini-2.5-flash"):
#         self.api_key = os.getenv("GEMINI_API_KEY")
#         if not self.api_key:
#             raise ValueError("GEMINI_API_KEY is missing. Set it in .env or GitHub Secrets.")
        
#         # New Google GenAI Client
#         self.client = genai.Client(api_key=self.api_key)
#         self.model_name = model_name

#     def generate_review(
#         self, 
#         prompt: str, 
#         system_instruction: Optional[str] = None, 
#         temperature: float = 0.2
#     ) -> str:
#         """Call Gemini API to generate PR review summary."""
        
#         sys_prompt = system_instruction or "You are an expert AI Code Reviewer and Security Auditor."
#         full_prompt = f"System Instruction: {sys_prompt}\n\nTask:\n{prompt}"

#         response = self.client.models.generate_content(
#             model=self.model_name,
#             contents=full_prompt,
#         )
#         return response.text










import os
from google import genai
from typing import Optional

class OpenAIProvider:
    """Provider wrapper for Google Gemini LLM inference."""
    
    def __init__(self, model_name: str = "gemma-4-26b-a4b-it"):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY is missing. Set it in .env or GitHub Secrets.")
        
        self.client = genai.Client(api_key=self.api_key)
        self.model_name = model_name

    def generate_review(
        self, 
        prompt: str, 
        system_instruction: Optional[str] = None, 
        temperature: float = 0.2
    ) -> str:
        sys_prompt = system_instruction or "You are an expert AI Code Reviewer and Security Auditor."
        full_prompt = f"System Instruction: {sys_prompt}\n\nTask:\n{prompt}"

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=full_prompt,
        )
        return response.text