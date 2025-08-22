"""Simple text analyzer agent that returns structured output."""

from typing import List, Dict, Any
from pydantic import BaseModel, Field
from agno.agent import Agent
from agno.models.anthropic import Claude
from demo.models.ai_model import sonnet_4, openai_gpt_4


def hello_world():
    """HELLO WORLD"""
    

    while True:
        print("\n📝 HELLO WORLD!:")
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
