# Bank Statement Processing Multi-Agent System

This demo showcases a sophisticated multi-agent system for processing bank statement PDFs with automatic validation and retry logic.

## System Overview

The system consists of three main components:

### 1. Extraction Agent (`extraction_agent.py`)
- **Purpose**: Analyzes PDF bank statements and extracts transaction data
- **Capabilities**:
  - Extracts text content from PDF files
  - Parses transactions (date, memo, amount)
  - Formats output as structured JSON
  - Handles reprocessing based on validation feedback

### 2. Validation Agent (`validation_agent.py`)
- **Purpose**: Validates extracted transaction data against the original PDF
- **Capabilities**:
  - Compares extracted data with original PDF content
  - Checks for format compliance and data integrity
  - Verifies amounts, dates, and memos match exactly
  - Identifies missing or incorrect transactions

### 3. Orchestrator (`bank_statement_orchestrator.py`)
- **Purpose**: Manages the multi-agent workflow with retry logic
- **Capabilities**:
  - Coordinates extraction and validation agents
  - Implements automatic retry loop until validation passes
  - Provides detailed logging and error handling
  - Returns structured results with processing status

## Key Features

### 🔄 Automatic Retry Logic
- If validation fails, the system automatically retries extraction
- Uses validation feedback to improve subsequent attempts
- Configurable maximum retry attempts (default: 3)

### ✅ Comprehensive Validation
- Format validation (JSON structure, required fields)
- Content validation (against original PDF)
- Amount accuracy verification
- Date format consistency checks

### 📊 Structured Output
Each transaction includes:
```json
{
  "date": "YYYY-MM-DD",
  "memo": "Transaction description",
  "amount": 123.45
}
```

### 🛡️ Error Handling
- Graceful handling of PDF processing errors
- Detailed error reporting and logging
- Fallback mechanisms for various failure scenarios

## Usage

### Basic Usage
```python
from demo.bank_statement_processing.bank_statement_orchestrator import BankStatementProcessingOrchestrator

# Initialize orchestrator
orchestrator = BankStatementProcessingOrchestrator(max_retries=3)

# Process bank statement
result = orchestrator.process_bank_statement("/path/to/statement.pdf")

if result['status'] == 'success':
    transactions = json.loads(result['extracted_transactions'])
    print(f"Extracted {len(transactions)} transactions")
else:
    print(f"Processing failed: {result.get('error')}")
```

### Running the Demo
```bash
cd /Users/k.yook/projects/agno
python demo/bank_statement_processing/bank_statement_demo.py
```

## File Structure

```
demo/bank_statement_processing/
├── __init__.py
├── README.md
├── bank_statement_demo.py          # Demo script
├── bank_statement_orchestrator.py  # Main orchestrator
├── agents/
│   ├── __init__.py
│   ├── extraction_agent.py         # PDF extraction agent
│   └── validation_agent.py         # Data validation agent
└── tools/
    ├── __init__.py
    └── pdf_tools.py                # PDF processing utilities
```

## Dependencies

For production use with real PDFs:
```bash
pip install PyPDF2  # For PDF text extraction
```

The demo works without additional dependencies using mock data.

## Workflow

1. **Extraction Phase**
   - Agent extracts text from PDF
   - Parses transactions into structured format
   - Returns JSON array of transactions

2. **Validation Phase**
   - Agent compares extracted data with original PDF
   - Validates format and content accuracy
   - Returns PASS/FAIL with detailed feedback

3. **Retry Logic**
   - If validation fails, extraction agent reprocesses
   - Uses validation feedback to improve accuracy
   - Continues until validation passes or max retries reached

## Configuration

The orchestrator supports several configuration options:

- `max_retries`: Maximum number of extraction attempts (default: 3)
- `enable_logging`: Enable detailed logging (default: True)

## Extension Points

The system is designed for easy extension:

- **Custom PDF Parsers**: Replace mock parsing in `pdf_tools.py`
- **Additional Validation Rules**: Extend validation logic in `validation_agent.py`
- **Different Output Formats**: Modify extraction agent output format
- **Enhanced Error Handling**: Add custom error handling logic

## Example Output

```
🏦 Bank Statement Processing Multi-Agent Demo
============================================================

✅ Status: SUCCESS
🎯 Completed in 1 attempt(s)

💰 Extracted Transactions (7 total):
--------------------------------------------------
 1. 2024-01-15 | +$5000.00 | Direct Deposit - SALARY
 2. 2024-01-16 |  -$200.00 | ATM Withdrawal
 3. 2024-01-17 |   -$89.99 | Online Purchase - AMAZON
 4. 2024-01-18 |  -$156.78 | Grocery Store Purchase
 5. 2024-01-19 |   -$45.20 | Gas Station
 6. 2024-01-22 |   -$67.43 | Restaurant
 7. 2024-01-25 |  -$234.56 | Utility Payment
--------------------------------------------------
    Net Amount: +$4206.04
```

This multi-agent system demonstrates sophisticated coordination between AI agents, automatic error recovery, and robust data validation - essential patterns for production financial data processing systems.