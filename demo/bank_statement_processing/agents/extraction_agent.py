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


class BankStatementExtractionAgent:
    """Agent specialized in extracting transaction data from bank statement PDFs."""
    
    def __init__(self, model=None):
        self.model = model or openai_gpt_4
        self.logger = logging.getLogger(__name__)
        
        self.agent = Agent(
            name="Bank Statement Extraction Agent",
            role="PDF Transaction Extractor",
            model=self.model,
            tools=[
                extract_text_from_pdf,
            ],
            instructions="""
            You are a specialized Bank Statement Extraction Agent focused on accurately extracting transaction data from PDF bank statements.
            
            Your responsibilities:
            1. Use extract_text_from_pdf tool with the provided PDF path to get the content
            2. Parse the text to identify individual transactions
            3. Extract date, memo/description, and amount for each transaction
            4. Return structured data using the TransactionList response model
            5. Handle various bank statement formats and layouts
            
            When processing bank statements:
            - First call extract_text_from_pdf with the PDF path provided in the message
            - Look for transaction patterns (dates, descriptions, amounts)
            - Pay attention to debit vs credit indicators
            - Ensure amounts are correctly signed (negative for debits, positive for credits)
            - Extract complete memo/description text
            - Use consistent date format (YYYY-MM-DD)
            - Handle currency symbols and formatting
            
            Response model requirements:
            - Use the TransactionList model which contains an array of Transaction objects
            - Each Transaction must have: date (YYYY-MM-DD), memo (string), amount (float)
            - Amount as number (negative for debits, positive for credits)
            
            Be thorough and accurate - this data will be validated by another agent.
            Make sure to extract all transactions from the statement.
            """,
            show_tool_calls=True,
            debug_mode=False,
            response_model=TransactionList
        )

    
    def reprocess_transactions(self, pdf_path: str, validation_feedback: str) -> str:
        """Reprocess transactions based on validation feedback."""
        self.logger.info("Reprocessing transactions...")
        prompt = f"""
        The previous transaction extraction failed validation with this feedback:
        {validation_feedback}
        
        Please re-extract transactions from the PDF at: {pdf_path}
        
        Address the validation issues by:
        1. Re-extracting the text content more carefully
        2. Double-checking transaction parsing logic
        3. Ensuring proper formatting and data types
        4. Verifying all required fields are present
        
        Focus on the specific issues mentioned in the validation feedback.
        Return only the corrected JSON array of transactions.
        """
        
        return self.agent.run(prompt)