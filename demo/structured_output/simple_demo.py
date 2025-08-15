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

from demo.structured_output.text_analyzer import TextAnalyzerAgent, demo_text_analyzer

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


def interactive_demo():
    """Run an interactive demo where users can input their own text."""
    print("\n🎮 INTERACTIVE MODE")
    print("=" * 40)
    print("Enter your own text to analyze (or 'quit' to exit):")
    
    analyzer = TextAnalyzerAgent()
    
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
            analysis = analyzer.analyze_text(user_text)
            
            # Save to file
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"text_analysis_{timestamp}.json"
            
            with open(output_file, 'w') as f:
                json.dump(analysis.model_dump(), f, indent=2, default=str)
            
            print(f"\n✅ Analysis complete! Results saved to: {output_file}")
            print(f"\n📊 Quick Summary:")
            print(f"  • Words: {analysis.word_count}")
            print(f"  • Sentiment: {analysis.sentiment.overall}")
            print(f"  • Topics: {len(analysis.key_topics)}")
            print(f"  • Reading Level: {analysis.reading_level}")
            
            # Ask if user wants to see full details
            show_details = input("\n🔍 Show detailed analysis? (y/n): ").lower().startswith('y')
            if show_details:
                print(f"\n💭 SENTIMENT BREAKDOWN:")
                print(f"  Positive: {analysis.sentiment.positive:.2f}")
                print(f"  Negative: {analysis.sentiment.negative:.2f}")
                print(f"  Neutral: {analysis.sentiment.neutral:.2f}")
                
                print(f"\n🎯 KEY TOPICS:")
                for topic in analysis.key_topics:
                    print(f"  • {topic.topic} (relevance: {topic.relevance:.2f})")
                
                print(f"\n📝 SUMMARY:")
                print(f"  {analysis.summary}")
                
        except Exception as e:
            print(f"❌ Analysis failed: {e}")


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
    print("1. Run predefined examples")
    print("2. Interactive mode (analyze your own text)")
    print("3. Both")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice in ['1', '3']:
        print("\n🏃 Running predefined examples...")
        demo_text_analyzer()
    
    if choice in ['2', '3']:
        interactive_demo()
    
    print("\n🎉 Demo completed!")
    print("\n💡 Key takeaways from this demo:")
    print("  • Single agent with structured output using Pydantic models")
    print("  • Type-safe responses with validation")
    print("  • Much simpler than multi-agent workflows")
    print("  • Perfect for API endpoints or data processing tasks")


if __name__ == "__main__":
    main()