"""Simple text analyzer agent that returns structured output."""

from typing import List, Dict, Any
from pydantic import BaseModel, Field
from agno.agent import Agent
from agno.models.anthropic import Claude
from demo.models.ai_model import sonnet_4, openai_gpt_4
from demo.text_analyzer.reviews import REVIEWS




class TextAnalyzerAgent:
    """Simple agent that analyzes text and returns structured output."""
    
    def __init__(self):
        """Initialize the text analyzer agent."""
        self.model = openai_gpt_4
        
        self.agent = Agent(
            name="Text Analyzer",
            role="Text Analysis Specialist", 
            model=self.model,
            instructions="""
            You are a text analysis specialist. Your job is to analyze any given text and provide comprehensive insights.
            
            For every text you analyze, provide:
            1. Basic statistics (word count, sentence count)
            2. Reading level assessment
            3. Sentiment analysis with detailed scores (positive, negative, neutral scores from 0-1, and overall sentiment)
            4. Key topics as a list, with separate lists for relevance scores and keywords for each topic
            5. A concise summary
            6. Main points extracted from the text
            
            Be accurate, thorough, and provide specific numerical scores where requested.
            Your analysis should be objective and data-driven.
            """,
            show_tool_calls=False,
            debug_mode=False,
        )

    
    def analyze_text(self, text: str) -> str:
        """
        Analyze the given text and return structured results.
        
        Args:
            text: The text to analyze
            
        Returns:
            TextAnalysis: Structured analysis results
        """
        prompt = f"""
        Please analyze the following text and provide a comprehensive analysis:

        TEXT TO ANALYZE:
        {text}

        """
        
        # Use the agent to generate structured output
        response = self.agent.print_response(
            prompt,
        )
        
        return response.content


def demo_text_analyzer():
    """Demonstrate the text analyzer with sample text."""
    analyzer = TextAnalyzerAgent()
    
    sample_texts = REVIEWS
    
    print("🔍 TEXT ANALYZER DEMO - Structured Output Example")
    print("=" * 60)
    
    for i, sample in enumerate(sample_texts, 1):
        print(f"\n📄 Example {i}: {sample['title']}")
        print("-" * 40)
        print(f"Text: {sample['text'][:100]}...")
        
        try:
            # Analyze the text
            analyzer.analyze_text(sample['text'])
            
        except Exception as e:
            print(f"❌ Analysis failed: {e}")
        
        if i < len(sample_texts):
            print("\n" + "=" * 60)


if __name__ == "__main__":
    demo_text_analyzer()