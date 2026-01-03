import os
import time
from openai import OpenAI
import logging

logger = logging.getLogger("research")

class LLMClient:
    def __init__(self, model="openai/gpt-4o-mini"):
        api_key = os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY")
        base_url = "https://openrouter.ai/api/v1" if os.getenv("OPENROUTER_API_KEY") else None
        
        if not api_key:
            raise ValueError("No API Key found")
            
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )
        self.model = model

    def generate(self, prompt, max_tokens=100):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens,
                temperature=0.0 # Deterministic
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"API Error: {e}")
            return "ERROR"
