"""
Abstract Base Class for LLM Providers.
"""

from abc import ABC, abstractmethod
from typing import Optional

class LLMProviderInterface(ABC):

    @abstractmethod
    def generate_review(
        self, 
        prompt: str, 
        system_instruction: Optional[str] = None,
        temperature: float = 0.2
    ) -> str:
        """
        Sends a prompt to the LLM and returns the text response.
        """
        pass