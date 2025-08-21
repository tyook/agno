"""Bank Statement Extraction Agent for analyzing PDFs and extracting transactions."""
import logging
from typing import List
from pydantic import BaseModel, Field
from agno.agent import Agent
from demo.models.ai_model import openai_gpt_4

class HelloWorldAgent:
    """Agent specialized in saying hello"""
    
    def __init__(self, model=None):
        self.model = model or openai_gpt_4
        self.logger = logging.getLogger(__name__)
        
        self.agent = Agent(
            name="Hello World Agent",
            role="Saying hello",
            model=self.model,
            instructions="""
            You are a specialized Hello World Agent focused on replying to make simple greetings.
            
            Your responsibilities:
            1. Provide greeting response to the user in a friendly manner.
            """,
            show_tool_calls=True,
            debug_mode=False,
        )
