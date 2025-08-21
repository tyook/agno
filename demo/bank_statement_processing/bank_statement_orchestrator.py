"""Bank Statement Processing Orchestrator with retry logic and validation feedback loop."""

import json
import logging
from typing import Dict, Any, Optional, List
from demo.bank_statement_processing.agents.extraction_agent import BankStatementExtractionAgent
from demo.bank_statement_processing.agents.validation_agent import BankStatementValidationAgent
from agno.workflow.v2 import Step, Workflow, StepOutput, StepInput, Loop, Condition

class BankStatementProcessingOrchestrator:
    """Orchestrator that manages the multi-agent workflow for bank statement processing."""
    
    def __init__(self, pdf_path: str, max_retries: int = 1):
        """
        Initialize the orchestrator.
        
        Args:
            max_retries: Maximum number of retry attempts for extraction
            enable_logging: Whether to enable detailed logging
        """
        self.max_retries = max_retries
        self.extraction_agent = BankStatementExtractionAgent()
        self.validation_agent = BankStatementValidationAgent()
        
        self.logger = logging.getLogger(__name__)
    
    def loop_end_validation_passes(self, step_output: List[StepOutput]) -> bool:
        """Check if validation passed by examining the validation step output."""
        self.logger.info("Loop end condition checking...")
        validation_output = step_output[1].content
        if validation_output:
            return "PASS" in str(validation_output).strip().upper()
        return False
    def _validation_passed(self, step_input: StepInput) -> bool:
        """Check if validation passed by examining the validation step output."""
        self.logger.info("Reprocess condition evaluating......")
        validation_output = step_input.get_step_output("validation")
        if validation_output and validation_output.content:
            passed = "PASS" in str(validation_output.content).strip().upper()
            self.logger.info( f"Validation passed: {passed}" if passed else f"Validation failed: {validation_output.content}")
            return passed
        return False
    
    def _extract_with_context(self, step_input: StepInput) -> StepOutput:
        """Extract transactions with access to workflow context."""
        pdf_path = step_input.additional_data.get("pdf_path") if step_input.additional_data else None
        
        self.logger.info(f"Extracting transactions from PDF: {pdf_path}")
        
        # Create a context-aware prompt for the extraction agent
        prompt = f"""
        Extract transactions from the bank statement PDF at: {pdf_path}
        
        Use the extract_text_from_pdf tool with the path: {pdf_path}
        Then parse the extracted text to identify all transactions and return them in the structured format.
        """
        
        result = self.extraction_agent.agent.run(prompt)
        return StepOutput(content=result.content if hasattr(result, 'content') else str(result))
    
    def _validate_with_context(self, step_input: StepInput) -> StepOutput:
        """Validate transactions with access to workflow context."""
        pdf_path = step_input.additional_data.get("pdf_path") if step_input.additional_data else None
        
        # Get the extraction result from the previous step
        extraction_output = step_input.get_step_content("extraction")
        
        self.logger.info(f"Validating transactions against PDF: {pdf_path}")
        
        # Create a context-aware prompt for the validation agent
        prompt = f"""
        Validate these extracted transactions against the original PDF at: {pdf_path}
        
        Extracted transactions to validate:
        {extraction_output}
        
        Use the extract_text_from_pdf tool with the path: {pdf_path} to get the original PDF content.
        Then compare the extracted transactions against the original content for accuracy.
        """
        
        result = self.validation_agent.agent.run(prompt)
        return StepOutput(content=result.content if hasattr(result, 'content') else str(result))

    def _reprocess_with_feedback(self, step_input: StepInput) -> StepOutput:
        """Reprocess transactions using validation feedback."""

        pdf_path = step_input.additional_data.get("pdf_path") if step_input.additional_data else None
        validation_feedback = step_input.get_step_content("validation")

        self.logger.info("Reprocessing with validation feedback...")
        
        # Use validation feedback for reprocessing
        extraction_response = self.extraction_agent.reprocess_transactions(
            pdf_path, validation_feedback
        )
        extraction_result = extraction_response.content if hasattr(extraction_response, 'content') else str(extraction_response)
        
        return StepOutput(content=extraction_result)
    
    def _create_workflow(self) -> Workflow:
        """Create the bank statement processing workflow."""
        return Workflow(
            name="Bank Statement Processing",
            description="Multi-agent workflow for bank statement extraction and validation with retry logic",
            steps=[
                Loop(
                    name="extraction_validation_loop",
                    max_iterations=self.max_retries,
                    end_condition=self.loop_end_validation_passes,
                    steps=[
                        Step(
                            name="extraction",
                            executor=self._extract_with_context,
                            max_retries=1,
                            description="Extract transactions from PDF"
                        ),
                        Step(
                            name="validation",
                            executor=self._validate_with_context,
                            max_retries=1,
                            description="Validate extracted transactions"
                        ),
                        Condition(
                            name="reprocess_if_failed",
                            evaluator=lambda step_input: not self._validation_passed(step_input),
                            steps=[
                                Step(
                                    name="reprocess",
                                    executor=self._reprocess_with_feedback,
                                    description="Reprocess transactions using validation feedback"
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    
    def process_bank_statement(self, pdf_path: str) -> Dict[str, Any]:
        """
        Process a bank statement PDF using agno workflow with retry logic and validation feedback.
        
        Args:
            pdf_path: Path to the bank statement PDF file
            
        Returns:
            Dictionary containing processing results and extracted transactions
        """
        self.logger.info(f"Starting bank statement processing workflow for: {pdf_path}")
        
        try:
            # Create and run the workflow
            workflow = self._create_workflow()
            result = workflow.run(
                message=f"Extract and validate transactions from bank statement PDF: {pdf_path}. The PDF path is: {pdf_path}",
                additional_data={"pdf_path": pdf_path}
            )
            
            # Extract results from workflow output
            if result and result.session_id:
                # Get the final validation result from step responses
                validation_output = None
                extraction_output = None
                
                # Look for the last successful extraction and validation in step_responses
                for step_result in result.step_responses:
                    if hasattr(step_result, 'step_name'):
                        if "validation" in step_result.step_name and step_result.content:
                            validation_output = step_result
                        elif "extraction" in step_result.step_name and step_result.content:
                            extraction_output = step_result
                
                if validation_output and "PASS" in str(validation_output.content).upper():
                    self.logger.info("Workflow completed successfully!")
                    return {
                        "status": "success",
                        "extracted_transactions": extraction_output.content if extraction_output else None,
                        "validation_result": validation_output.content,
                        "pdf_path": pdf_path,
                        "session_id": result.session_id
                    }
                else:
                    self.logger.error("Workflow completed but validation failed")
                    return {
                        "status": "failed",
                        "extracted_transactions": extraction_output.content if extraction_output else None,
                        "validation_result": validation_output.content if validation_output else "No validation result",
                        "error": "Validation failed after maximum retries",
                        "pdf_path": pdf_path,
                        "session_id": result.session_id
                    }
            else:
                self.logger.error("Workflow execution failed")
                return {
                    "status": "error",
                    "error": "Workflow execution failed - no result returned",
                    "pdf_path": pdf_path
                }
                
        except Exception as e:
            self.logger.error(f"Error during workflow execution: {str(e)}")
            return {
                "status": "error",
                "error": f"Workflow execution error: {str(e)}",
                "pdf_path": pdf_path
            }
    
    def _create_format_validation_workflow(self, extracted_transactions: str) -> Workflow:
        """Create a simple workflow for format validation."""
        return Workflow(
            name="Quick Format Validation",
            description="Validate transaction format without PDF comparison",
            steps=[
                Step(
                    name="format_validation",
                    agent=self.validation_agent.agent,
                    max_retries=1,
                    description="Quick format validation"
                )
            ]
        )
    
    def quick_format_check(self, extracted_transactions: str) -> Dict[str, Any]:
        """
        Perform a quick format validation using agno workflow without full PDF comparison.
        
        Args:
            extracted_transactions: JSON string of extracted transactions
            
        Returns:
            Dictionary containing format validation results
        """
        self.logger.info("Performing quick format validation with workflow...")
        
        try:
            # Create and run the format validation workflow
            workflow = self._create_format_validation_workflow(extracted_transactions)
            result = workflow.run(
                message=f"Perform quick format validation on these transactions: {extracted_transactions}",
                additional_data={"transactions": extracted_transactions}
            )
            
            if result and result.session_id:
                # Get the validation result from step responses
                validation_output = None
                for step_result in result.step_responses:
                    if hasattr(step_result, 'step_name') and "format_validation" in step_result.step_name and step_result.content:
                        validation_output = step_result
                        break
                
                if validation_output:
                    validation_result = validation_output.content
                    return {
                        "status": "success" if "FORMAT_PASS" in str(validation_result) else "failed",
                        "validation_result": validation_result,
                        "extracted_transactions": extracted_transactions,
                        "session_id": result.session_id
                    }
                else:
                    return {
                        "status": "error",
                        "error": "No validation output received from workflow",
                        "extracted_transactions": extracted_transactions
                    }
            else:
                return {
                    "status": "error", 
                    "error": "Format validation workflow execution failed",
                    "extracted_transactions": extracted_transactions
                }
                
        except Exception as e:
            self.logger.error(f"Error during format validation workflow: {str(e)}")
            return {
                "status": "error",
                "error": f"Format validation workflow error: {str(e)}",
                "extracted_transactions": extracted_transactions
            }
    
    def get_processing_stats(self) -> Dict[str, Any]:
        """Get statistics about the orchestrator configuration."""
        return {
            "max_retries": self.max_retries,
            "extraction_agent": self.extraction_agent.__class__.__name__,
            "validation_agent": self.validation_agent.__class__.__name__
        }


def main():
    """Example usage of the bank statement processing orchestrator."""
    pdf_path = "/path/to/your/bank_statement.pdf"
    # Initialize orchestrator
    orchestrator = BankStatementProcessingOrchestrator(max_retries=1, pdf_path=pdf_path)
    
    # Example PDF path (you would replace this with actual PDF path)
    
    
    print("Bank Statement Processing Orchestrator Demo")
    print("=" * 50)
    
    # Process the bank statement
    result = orchestrator.process_bank_statement(pdf_path)
    
    print(f"Processing Status: {result['status']}")
    print(f"Attempts Made: {result.get('attempt', 'N/A')}")
    
    if result['status'] == 'success':
        print("✅ Processing completed successfully!")
        print(f"Validation Result: {result['validation_result']}")
        
        # Try to parse and display transactions
        try:
            transactions = json.loads(result['extracted_transactions'])
            print(f"\nExtracted {len(transactions)} transactions:")
            for i, txn in enumerate(transactions, 1):
                print(f"{i}. {txn['date']} | {txn['memo']} | ${txn['amount']}")
        except:
            print("Could not parse extracted transactions for display")
    
    else:
        print("❌ Processing failed!")
        if 'error' in result:
            print(f"Error: {result['error']}")
        if 'validation_result' in result:
            print(f"Last Validation Result: {result['validation_result']}")


if __name__ == "__main__":
    main()