"""Bank Statement Validation Agent for verifying extracted transaction data."""

from pydantic import BaseModel, Field
from agno.agent import Agent
from demo.models.ai_model import openai_gpt_4
from demo.bank_statement_processing.tools.pdf_tools import extract_text_from_pdf, validate_transaction_format


class ValidationResult(BaseModel):
    """Validation result with status and reason."""
    status: str = Field(..., description="Validation status: PASS or FAIL")
    reason: str = Field(..., description="Detailed explanation of validation result")


class BankStatementValidationAgent:
    """Agent specialized in validating extracted transaction data against original PDF."""
    
    def __init__(self, model=None):
        self.model = model or openai_gpt_4

        
        self.agent = Agent(
            name="Bank Statement Validation Agent",
            role="Transaction Data Validator",
            model=self.model,
            tools=[
                extract_text_from_pdf,
                validate_transaction_format
            ],
            instructions="""
            You are a specialized Bank Statement Validation Agent focused on verifying the accuracy of extracted transaction data.
            
            Your responsibilities:
            1. Validate extracted transaction data against the original PDF
            2. Check for format compliance and data integrity
            3. Verify that all transactions are correctly extracted
            4. Ensure amounts, dates, and memos match the PDF exactly
            5. Identify any discrepancies or missing transactions
            
            IMPORTANT: When you receive a validation request:
            1. Use the extract_text_from_pdf tool with the PDF path provided in the message
            2. Compare the extracted transactions against the PDF content
            3. Use the validate_transaction_format tool to check JSON format
            
            Validation criteria:
            - All transactions in PDF are captured in the JSON
            - No extra transactions that aren't in the PDF
            - Amounts match exactly (including sign - debit/credit)
            - Dates are correct and properly formatted
            - Memo descriptions are accurate and complete
            - JSON format is valid and follows required schema
            
            When validating:
            - First call extract_text_from_pdf with the PDF path to get the original PDF text
            - Compare line by line against the original PDF text
            - Check for typos in memo descriptions
            - Verify arithmetic accuracy of amounts
            - Ensure no transactions are duplicated or missed
            - Validate date parsing is correct
            
            Use the ValidationResult response model with:
            - status: "PASS" if all validations succeed, "FAIL" if validation fails
            - reason: Detailed explanation of validation result or specific issues found
            
            Be thorough and precise - incorrect data could cause financial discrepancies.
            """,
            show_tool_calls=True,
            debug_mode=False,
            response_model=ValidationResult
        )
    
    
    def quick_format_validation(self, extracted_transactions: str) -> str:
        """Perform quick format validation without PDF comparison."""
        prompt = f"""
        Please perform a quick format validation on the extracted transaction data:
        
        Extracted Transactions: {extracted_transactions}
        
        Validate:
        1. JSON format is valid
        2. All required fields are present (date, memo, amount)
        3. Data types are correct
        4. Date format follows YYYY-MM-DD pattern
        5. Amounts are numeric values
        
        Return:
        - "FORMAT_PASS" if format validation succeeds
        - "FORMAT_FAIL: [specific format issues]" if validation fails
        """
        
        return self.agent.run(prompt)