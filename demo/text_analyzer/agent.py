"""Bank Statement Extraction Agent for analyzing PDFs and extracting transactions."""
import logging
from typing import List
from pydantic import BaseModel, Field
from agno.agent import Agent
from demo.models.ai_model import openai_gpt_4
from demo.bank_statement_processing.tools.pdf_tools import extract_text_from_pdf


class Transaction(BaseModel):
    """Individual transaction data."""
    date: str = Field(..., description="Transaction date in YYYY-MM-DD format")
    memo: str = Field(..., description="Transaction memo/description")
    amount: float = Field(..., description="Transaction amount (negative for debits, positive for credits)")


class TransactionList(BaseModel):
    """List of extracted transactions."""
    transactions: List[Transaction] = Field(..., description="Array of extracted transactions")


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
