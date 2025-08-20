#!/usr/bin/env python3
"""Simple demonstration of Agno's Team API functionality."""

import os
import sys
import warnings
from datetime import datetime
from dotenv import load_dotenv
import json
# Suppress httpx client cleanup warnings
warnings.filterwarnings("ignore", message=".*SyncHttpxClientWrapper.*")

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from agno.team import Team
from agno.agent import Agent
from demo.models.ai_model import sonnet_4, openai_gpt_4

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

def create_simple_team_demo():
    """Demonstrate basic Team API functionality with a simple use case."""
    
    # Create individual agents with different roles
    researcher = Agent(
        name="Researcher",
        role="Research Specialist",
        instructions="You are a research specialist. Focus on gathering facts, data, and insights on any given topic.",
        model=openai_gpt_4
    )
    
    analyst = Agent(
        name="Analyst", 
        role="Data Analyst",
        instructions="You are a data analyst. Focus on analyzing information, identifying patterns, and drawing conclusions.",
        model=openai_gpt_4
    )
    
    writer = Agent(
        name="Writer",
        role="Content Writer", 
        instructions="You are a content writer. Focus on creating clear, engaging, and well-structured content.",
        model=openai_gpt_4
    )
    
    # Create a team with these agents
    team = Team(
        members=[researcher, analyst, writer],
        show_tool_calls=True,
        model=openai_gpt_4
    )
    
    return team

def run_team_collaboration_demo():
    """Run a demonstration of team collaboration."""
    
    print("🚀 Creating Team Demo...")
    team = create_simple_team_demo()
    
    print("👥 Team Members:")
    for agent in team.members:
        print(f"  - {agent.name} ({agent.role})")
    
    print("\n💬 Starting team collaboration on: 'The future of renewable energy'")
    print("=" * 60)
    
    # Run a collaborative task
    prompt = """
    Topic: The future of renewable energy
    
    Please work together to provide insights on this topic:
    - Researcher: Gather current facts and trends
    - Analyst: Analyze the data and identify key patterns
    - Writer: Create a summary of the findings
    
    Each team member should contribute from their expertise area.
    """
    
    response = team.run(prompt)
    
    print("\n📋 Team Collaboration Result:")
    print("-" * 40)
    print(response)
    
    return response

def run_focused_team_task():
    """Run a more focused team task demonstration."""
    
    team = create_simple_team_demo()
    
    print("\n🎯 Running Focused Team Task...")
    print("Topic: Best practices for remote work productivity")
    print("=" * 60)
    
    focused_prompt = """
    We need to create actionable advice for remote work productivity.
    
    Researcher: Find evidence-based productivity strategies
    Analyst: Evaluate which strategies are most effective and why
    Writer: Create a clear, actionable list of recommendations
    
    Please collaborate to provide practical advice.
    """
    
    response = team.run(focused_prompt)
    
    print("\n📝 Focused Task Result:")
    print("-" * 40)
    print(response)

    output_file = f"interactive_demo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, 'w') as f:
        json.dump(response, f, indent=2, default=str)
        
    print(f"\\n📄 Results saved to: {output_file}")
    
    return response

if __name__ == "__main__":
    print("🔧 Agno Team API Demo")
    print("=" * 50)
    
    if not check_api_key():
        sys.exit(1)
    
    # Run the collaboration demo
    run_team_collaboration_demo()
    
    # Run a focused task
    run_focused_team_task()
    
    print("\n✅ Demo completed!")