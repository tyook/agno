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

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


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
    
    
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice in ['0']:
        print("\n🏃 Running predefined examples...")
        hello_world()
    if choice in ['1']:
        print("\n🏃 Running predefined examples...")
        # demo_text_analyzer()
    
    
    print("\n🎉 Demo completed!")
    print("\n💡 Key takeaways from this demo:")
    print("  • Single agent with structured output using Pydantic models")
    print("  • Type-safe responses with validation")
    print("  • Much simpler than multi-agent workflows")
    print("  • Perfect for API endpoints or data processing tasks")


if __name__ == "__main__":
    main()