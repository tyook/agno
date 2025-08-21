"""Simple text analyzer agent that returns structured output."""

from typing import List, Dict, Any
from pydantic import BaseModel, Field
from agno.agent import Agent
from agno.models.anthropic import Claude
from demo.models.ai_model import sonnet_4, openai_gpt_4


class HelloWorldAgent:
    """Simple agent that analyzes text and returns structured output."""

    def __init__(self):
        """Initialize the text analyzer agent."""
        self.model = openai_gpt_4

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



def hello_world():
    """Demonstrate the text analyzer with sample text."""
    

    while True:
        print("\n📝 Enter text to analyze:")
        user_text = input("> ")

        if user_text.lower() in ['quit', 'exit', 'q']:
            print("👋 Goodbye!")
            break

        if len(user_text.strip()) < 10:
            print("⚠️  Please enter at least 10 characters of text.")
            continue

        try:
            print("\n🔄 Analyzing...")
            

        except Exception as e:
            print(f"❌ Analysis failed: {e}")


if __name__ == "__main__":
    hello_world()
