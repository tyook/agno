"""
Bank Statement Processing Demo

This demo showcases a multi-agent system for processing bank statement PDFs:
1. Extraction Agent: Analyzes PDF and extracts transactions as JSON
2. Validation Agent: Validates extracted data against original PDF
3. Orchestrator: Manages retry logic until validation passes

Usage:
    python demo/bank_statement_processing/bank_statement_demo.py
"""

import json
import os
import sys
import json
import warnings
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path


# Suppress httpx client cleanup warnings
warnings.filterwarnings("ignore", message=".*SyncHttpxClientWrapper.*")

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Load environment variables
load_dotenv()

from demo.bank_statement_processing.bank_statement_orchestrator import BankStatementProcessingOrchestrator

def demo_bank_statement_processing():
    """Run the bank statement processing demo."""
    print("🏦 Bank Statement Processing Multi-Agent Demo")
    print("=" * 60)
    print()
    
    print("This demo showcases a multi-agent system with:")
    print("1. 📄 Extraction Agent - Extracts transactions from PDF")
    print("2. ✅ Validation Agent - Validates extraction accuracy")
    print("3. 🔄 Orchestrator - Manages retry loop until validation passes")
    print()
    
    
    demo_pdf_path = "demo/bank_statement_processing/sample_txn.pdf"

    # Initialize the orchestrator
    orchestrator = BankStatementProcessingOrchestrator(pdf_path=demo_pdf_path, max_retries=1)
    
    print("🚀 Initializing Multi-Agent System...")
    stats = orchestrator.get_processing_stats()
    print(f"   - Max Retries: {stats['max_retries']}")
    print(f"   - Extraction Agent: {stats['extraction_agent']}")
    print(f"   - Validation Agent: {stats['validation_agent']}")
    print()
    
    
    
    print(f"📋 Processing Bank Statement: {demo_pdf_path}")
    
    # Process the bank statement
    print("🔄 Starting Multi-Agent Processing Pipeline...")
    result = orchestrator.process_bank_statement(demo_pdf_path)
    
    print()
    print("📊 Processing Results:")
    print("=" * 30)
    
    if result['status'] == 'success':
        print("✅ Status: SUCCESS")
        print(f"🎯 Completed in {result['attempt']} attempt(s)")
        print(f"✓ Validation: {result['validation_result']}")
        print()
        
        # Display extracted transactions
        try:
            transactions = json.loads(result['extracted_transactions'])
            print(f"💰 Extracted Transactions ({len(transactions)} total):")
            print("-" * 50)
            
            total_amount = 0
            for i, txn in enumerate(transactions, 1):
                amount_str = f"${txn['amount']:+.2f}"
                print(f"{i:2d}. {txn['date']} | {amount_str:>10} | {txn['memo']}")
                total_amount += txn['amount']
            
            print("-" * 50)
            print(f"    Net Amount: ${total_amount:+.2f}")
            
        except json.JSONDecodeError:
            print("⚠️  Could not parse extracted transactions for display")
            print(f"Raw output: {result['extracted_transactions']}")
    
    elif result['status'] == 'failed':
        print("❌ Status: FAILED")
        
        print(f"❗ Error: {result.get('error', 'Validation failed after maximum retries')}")
        
        if 'validation_result' in result:
            print(f"📋 Last Validation Result: {result['validation_result']}")
    
    else:
        print("💥 Status: ERROR")
        print(f"❗ Error: {result.get('error', 'Unknown error occurred')}")
    
    print()
    print("🎯 Demo Features Demonstrated:")
    print("   ✓ Multi-agent coordination")
    print("   ✓ Automatic retry logic")
    print("   ✓ Validation feedback loop")
    print("   ✓ Error handling and logging")
    print("   ✓ Structured data extraction")
    
    return result


def demo_quick_format_validation():
    """Demo the quick format validation feature."""
    print("\n" + "=" * 60)
    print("📋 Quick Format Validation Demo")
    print("=" * 60)
    
    orchestrator = BankStatementProcessingOrchestrator(pdf_path="demo/bank_statement_processing/sample_txn.pdf")
    
    # Sample valid JSON
    valid_json = json.dumps([
        {"date": "2024-01-15", "memo": "Salary", "amount": 5000.00},
        {"date": "2024-01-16", "memo": "ATM", "amount": -200.00}
    ], indent=2)
    
    print("Testing valid transaction format...")
    result = orchestrator.quick_format_check(valid_json)
    print(f"Result: {result['status']}")
    print(f"Details: {result.get('validation_result', result.get('error', 'No details available'))}")
    
    # Sample invalid JSON
    print("\nTesting invalid transaction format...")
    invalid_json = '{"invalid": "format"}'
    result = orchestrator.quick_format_check(invalid_json)
    print(f"Result: {result['status']}")
    print(f"Details: {result.get('validation_result', result.get('error', 'No details available'))}")


if __name__ == "__main__":
    # Run the main demo
    demo_result = demo_bank_statement_processing()
    
    # Run the format validation demo
    demo_quick_format_validation()
    
    print("\n" + "🎉 Bank Statement Processing Demo Complete! 🎉")
    print("\nTo use with real PDFs:")
    print("1. Install PyPDF2: pip install PyPDF2")
    print("2. Update pdf_tools.py with real PDF parsing logic")
    print("3. Provide actual PDF file paths to the orchestrator")
    print("\nThe system will automatically retry extraction until validation passes!")