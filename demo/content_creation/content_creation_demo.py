#!/usr/bin/env python3
"""
Agno Multi-Agent Content Creation Demo

This demo showcases a complete AI-powered content creation agency using the agno framework.
It demonstrates multiple specialized agents working together through coordinated workflows.
"""

import os
import sys
import json
import warnings
from datetime import datetime, timedelta
from typing import Optional
from dotenv import load_dotenv

# Suppress httpx client cleanup warnings
warnings.filterwarnings("ignore", message=".*SyncHttpxClientWrapper.*")

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from demo.content_creation.workflows.content_creation_workflow import ContentCreationWorkflow

# Load environment variables
load_dotenv()


def print_banner():
    """Print the demo banner."""
    print("=" * 80)
    print("🤖 AGNO MULTI-AGENT CONTENT CREATION AGENCY DEMO")
    print("=" * 80)
    print("Showcasing coordinated AI agents working together to create high-quality content")
    print()


def print_agent_intro():
    """Print introduction to the agents."""
    print("👥 MEET THE TEAM:")
    print()
    print("🔍 Research Agent - Gathers information and insights on topics")
    print("📋 Content Strategist - Plans content strategy and defines requirements") 
    print("✍️  Writer Agent - Creates engaging and well-structured content")
    print("📖 Editor Agent - Reviews, edits, and ensures quality standards")
    print("🎯 Project Manager - Coordinates workflow and manages deliverables")
    print()


def run_quick_demo():
    """Run a quick demonstration with a predefined topic."""
    print("🚀 RUNNING QUICK DEMO: AI in Healthcare")
    print("-" * 50)
    
    try:
        # Initialize the workflow
        workflow = ContentCreationWorkflow()
        
        # Run the complete workflow
        results = workflow.run_complete_workflow(
            topic="AI in Healthcare",
            content_type="blog_post",
            target_audience="healthcare professionals and technology enthusiasts",
            deadline=(datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
        )
        
        # Generate and display report
        report = workflow.generate_workflow_report(results)
        print(report)
        
        # Save results to file
        output_file = f"demo_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        
        print(f"\\n📄 Detailed results saved to: {output_file}")
        
        return results
        
    except Exception as e:
        print(f"❌ Demo failed: {str(e)}")
        print("\\n💡 Make sure you have set up your API keys in a .env file:")
        print("   ANTHROPIC_API_KEY=your_key_here")
        return None


def run_interactive_demo():
    """Run an interactive demo where users can specify parameters."""
    print("🎮 INTERACTIVE DEMO MODE")
    print("-" * 30)
    
    try:
        # Get user inputs
        topic = input("Enter content topic: ").strip()
        if not topic:
            topic = "Artificial Intelligence in Modern Business"
            print(f"Using default topic: {topic}")
        
        print("\\nContent type options: blog_post, article, social_media")
        content_type = input("Enter content type (default: blog_post): ").strip()
        if not content_type:
            content_type = "blog_post"
        
        target_audience = input("Enter target audience (default: general): ").strip()
        if not target_audience:
            target_audience = "general"
        
        print(f"\\n🎯 Creating content about '{topic}' as a {content_type} for {target_audience}")
        print("\\n" + "="*60)
        
        # Initialize and run workflow
        workflow = ContentCreationWorkflow()
        results = workflow.run_complete_workflow(
            topic=topic,
            content_type=content_type,
            target_audience=target_audience
        )
        
        # Display results
        report = workflow.generate_workflow_report(results)
        print(report)
        
        # Save results
        output_file = f"interactive_demo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        
        print(f"\\n📄 Results saved to: {output_file}")
        
        return results
        
    except KeyboardInterrupt:
        print("\\n\\n👋 Demo cancelled by user")
        return None
    except Exception as e:
        print(f"\\n❌ Demo failed: {str(e)}")
        return None


def run_collaborative_demo():
    """Run a collaborative demo showing agents working together."""
    print("🤝 COLLABORATIVE DEMO MODE")
    print("-" * 35)
    
    try:
        workflow = ContentCreationWorkflow()
        
        # Example collaborative challenges
        challenges = [
            {
                "topic": "Remote Work Productivity",
                "challenge": "How can we make this content engaging for both managers and remote employees?"
            },
            {
                "topic": "Cybersecurity Best Practices", 
                "challenge": "How do we balance technical accuracy with accessibility for non-technical readers?"
            },
            {
                "topic": "Sustainable Technology",
                "challenge": "What unique angle can we take that hasn't been covered extensively already?"
            }
        ]
        
        print("Available collaborative challenges:")
        for i, challenge in enumerate(challenges, 1):
            print(f"{i}. {challenge['topic']}: {challenge['challenge']}")
        
        choice = input("\\nSelect a challenge (1-3) or enter your own topic: ").strip()
        
        if choice.isdigit() and 1 <= int(choice) <= 3:
            selected = challenges[int(choice) - 1]
            topic = selected["topic"]
            challenge = selected["challenge"]
        else:
            topic = choice if choice else "Digital Transformation"
            challenge = input("Enter specific challenge/question: ").strip()
            if not challenge:
                challenge = "How can we create content that stands out in a crowded market?"
        
        print(f"\\n🎯 Topic: {topic}")
        print(f"🤔 Challenge: {challenge}")
        print("\\n" + "="*60)
        
        # Run collaborative session
        response = workflow.run_collaborative_session(topic, challenge)
        
        print("\\n🤝 COLLABORATIVE TEAM RESPONSE:")
        print("-" * 45)
        print(response)

        # Save results to file
        output_file = f"demo_collab_team_responseoutput_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(output_file, 'w') as f:
            json.dump(response, f, indent=2, default=str)
        
        print(f"\\n📄 Detailed results saved to: {output_file}")
        
        return response
        
    except Exception as e:
        print(f"\\n❌ Collaborative demo failed: {str(e)}")
        return None


def main():
    """Main demo function."""
    print_banner()
    print_agent_intro()
    
    # Check for API keys
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("⚠️  WARNING: No ANTHROPIC_API_KEY found in environment variables.")
        print("   Copy .env.example to .env and add your API key to run the demo.")
        print("   Continuing with demo structure (agents may not function properly)\\n")
    
    print("🎮 DEMO OPTIONS:")
    print("1. Quick Demo - Predefined 'AI in Healthcare' content creation")
    print("2. Interactive Demo - Choose your own topic and parameters")
    print("3. Collaborative Demo - See agents working together on challenges")
    print("4. Show Agent Details - Learn more about each agent's capabilities")
    print("5. Exit")
    
    while True:
        try:
            choice = input("\\nSelect demo option (1-5): ").strip()
            
            if choice == "1":
                print("\\n" + "="*80)
                run_quick_demo()
                break
                
            elif choice == "2":
                print("\\n" + "="*80)
                run_interactive_demo()
                break
                
            elif choice == "3":
                print("\\n" + "="*80)
                run_collaborative_demo()
                break
                
            elif choice == "4":
                show_agent_details()
                
            elif choice == "5":
                print("\\n👋 Thanks for trying the Agno Multi-Agent Demo!")
                break
                
            else:
                print("❌ Invalid choice. Please select 1-5.")
                
        except KeyboardInterrupt:
            print("\\n\\n👋 Demo cancelled. Goodbye!")
            break
        except Exception as e:
            print(f"\\n❌ Unexpected error: {str(e)}")
            break


def show_agent_details():
    """Show detailed information about each agent."""
    print("\\n" + "="*80)
    print("🤖 AGENT CAPABILITIES BREAKDOWN")
    print("="*80)
    
    agents_info = [
        {
            "name": "🔍 Research Agent",
            "role": "Information Researcher and Analyst",
            "tools": ["Web Search Tool", "Trend Analysis Tool", "Fact Check Tool"],
            "capabilities": [
                "Conduct thorough research on assigned topics",
                "Analyze trends and market data",
                "Fact-check information and verify claims",
                "Identify key themes and emerging trends"
            ]
        },
        {
            "name": "📋 Content Strategist Agent", 
            "role": "Content Strategy and Planning Specialist",
            "tools": ["Content Planner Tool", "SEO Optimizer Tool"],
            "capabilities": [
                "Develop comprehensive content strategies",
                "Create detailed content outlines",
                "Define target audiences and messaging",
                "Optimize content for SEO and discoverability"
            ]
        },
        {
            "name": "✍️ Writer Agent",
            "role": "Content Writer and Creator", 
            "tools": ["Writing Quality Tool"],
            "capabilities": [
                "Write compelling and well-structured content",
                "Adapt tone and style to target audience",
                "Create engaging headlines and calls-to-action",
                "Optimize content for readability"
            ]
        },
        {
            "name": "📖 Editor Agent",
            "role": "Content Editor and Quality Assurance",
            "tools": ["Writing Quality Tool", "SEO Optimizer Tool", "Fact Check Tool"],
            "capabilities": [
                "Review content for grammar and clarity",
                "Ensure factual accuracy",
                "Optimize content structure and flow", 
                "Check SEO compliance and quality standards"
            ]
        },
        {
            "name": "🎯 Project Manager Agent",
            "role": "Project Coordinator and Workflow Manager",
            "tools": ["Task Manager Tool", "Progress Tracker Tool", "Communication Tool"],
            "capabilities": [
                "Plan and organize content projects",
                "Create and assign tasks to team members",
                "Track progress and manage timelines",
                "Coordinate communication and deliverables"
            ]
        }
    ]
    
    for agent in agents_info:
        print(f"\\n{agent['name']}")
        print(f"Role: {agent['role']}")
        print(f"Tools: {', '.join(agent['tools'])}")
        print("Key Capabilities:")
        for capability in agent['capabilities']:
            print(f"  • {capability}")
        print("-" * 60)
    
    input("\\nPress Enter to return to main menu...")


if __name__ == "__main__":
    main()