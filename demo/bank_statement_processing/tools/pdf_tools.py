"""PDF processing tools for bank statement analysis."""

import json
from typing import List, Dict, Any
from agno.tools import tool



@tool
def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text content from a PDF file.
    
    Args:
        pdf_path: Path to the PDF file
        
    Returns:
        Extracted text content as string
    """
    try:
        import PyPDF2
        
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
                
        return text.strip()
    except ImportError:
        return "Error: PyPDF2 not installed. Please install with: pip install PyPDF2"
    except Exception as e:
        return f"Error extracting text from PDF: {str(e)}"



@tool
def validate_transaction_format(original_transaction_data: str, target_transaction_data: str) -> str:
    """
    Validate that transaction data follows the expected JSON format.
    
    Args:
        transaction_data: JSON string containing transaction data
        
    Returns:
        Validation result as string
    """
    try:
        transactions = json.loads(target_transaction_data)
        
        if not isinstance(transactions, list):
            return "Error: Transaction data must be a list"
            
        for i, txn in enumerate(transactions):
            if not isinstance(txn, dict):
                return f"Error: Transaction {i} is not a dictionary"
                
            required_fields = ["date", "memo", "amount"]
            for field in required_fields:
                if field not in txn:
                    return f"Error: Transaction {i} missing required field '{field}'"
                    
            # Validate date format (basic check)
            date_str = txn["date"]
            if not isinstance(date_str, str) or len(date_str.split("-")) != 3:
                return f"Error: Transaction {i} has invalid date format"
                
            # Validate amount is numeric
            if not isinstance(txn["amount"], (int, float)):
                return f"Error: Transaction {i} has non-numeric amount"
                
        return f"Validation passed: {len(transactions)} transactions validated successfully"
        
    except json.JSONDecodeError:
        return "Error: Invalid JSON format"
    except Exception as e:
        return f"Error during validation: {str(e)}"