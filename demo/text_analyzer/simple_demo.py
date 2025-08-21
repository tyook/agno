#!/usr/bin/env python3
"""
Simple Structured Output Demo

This demo shows how to use agno agents to generate structured output using Pydantic models.
It's a much simpler example compared to the content creation workflow, focusing on 
a single agent that analyzes text and returns structured data.
"""

import os
import sys
import json
import warnings
from datetime import datetime
from dotenv import load_dotenv

# Suppress httpx client cleanup warnings
warnings.filterwarnings("ignore", message=".*SyncHttpxClientWrapper.*")


from demo.text_analyzer.hello_world import hello_world

from demo.text_analyzer.text_analyzer import TextAnalyzerAgent, demo_text_analyzer
from demo.text_analyzer.text_analyzer_structured import demo_text_analyzer_structured
from demo.text_analyzer.text_analyzer_tool import demo_text_analyzer_with_tool
from demo.text_analyzer.text_analyzer_team import demo_review_reply_with_team
from demo.text_analyzer.hello_world import hello_world


# Load environment variables
load_dotenv()


def check_api_key():
    """Check if the API key is set."""
    if not os.getenv("AWS_BEDROCK_ACCESS_KEY_ID"):
        print("⚠️  WARNING: No AWS_BEDROCK_ACCESS_KEY_ID found in environment variables.")
        print("   Please set your API key in the .env file:")
        print("   AWS_BEDROCK_ACCESS_KEY_ID=your_key_here")
        print("   Or export it as an environment variable.")
        return False
    return True

def main():
    """Main demo function."""
    print("🚀 AGNO SIMPLE STRUCTURED OUTPUT DEMO")
    print("=" * 50)
    print("This demo shows how to create agents that return structured data")
    print("using Pydantic models for type safety and validation.")
    print()
    
    if not check_api_key():
        return
    
    print("Choose a demo mode:")
    print("0. Hello World")

    choice = input("\nEnter your choice: ").strip()
    
    if choice in ['0']:
        print("\n🏃 Running hello world...")
        hello_world()

    print("1. text analyzer basic")
    print("2. text analyzer with structured output")
    print("3. text analyzer with tools")
    print("4. text analyzer with reviews")
    
    choice = input("\nEnter your choice (0-4): ").strip()
    
    if choice in ['0']:
        print("\n🏃 Running predefined examples...")
        hello_world()
    if choice in ['1']:
        print("\n🏃 Running text analyzer basic...")
        demo_text_analyzer()
    if choice in ['2']:
        print("\n🏃 text analyzer with structured output...")
        demo_text_analyzer_structured()
    if choice in ['3']:
        print("\n🏃 text analyzer with tools...")
        demo_text_analyzer_with_tool()
    if choice in ['4']:
        print("\n🏃 text analyzer with reviews...")
        demo_review_reply_with_team()
           

    print("\n🎉 Demo completed!")
    print("\n💡 Key takeaways from this demo:")
    print("  • Single agent with structured output using Pydantic models")
    print("  • Type-safe responses with validation")
    print("  • Much simpler than multi-agent workflows")
    print("  • Perfect for API endpoints or data processing tasks")


if __name__ == "__main__":
    main()