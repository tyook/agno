"""
Basic usage examples for the Agno Multi-Agent Content Creation Demo.

This file demonstrates how to use the various components of the system programmatically.
"""

import sys
import os
from datetime import datetime, timedelta

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from demo.workflows.content_creation_workflow import ContentCreationWorkflow
from demo.agents.research_agent import ResearchAgent
from demo.agents.strategist_agent import ContentStrategistAgent
from demo.agents.writer_agent import WriterAgent
from demo.agents.editor_agent import EditorAgent
from demo.agents.project_manager_agent import ProjectManagerAgent


def example_complete_workflow():
    """Example: Run a complete content creation workflow."""
    print("="*60)
    print("EXAMPLE 1: Complete Content Creation Workflow")
    print("="*60)
    
    # Initialize workflow
    workflow = ContentCreationWorkflow()
    
    # Run workflow with custom parameters
    results = workflow.run_complete_workflow(
        topic="Machine Learning in Finance",
        content_type="article",
        target_audience="financial professionals and data scientists",
        deadline=(datetime.now() + timedelta(days=10)).strftime("%Y-%m-%d")
    )
    
    # Display summary
    if "error" not in results:
        print("✅ Workflow completed successfully!")
        print(f"📊 Generated {len(results['workflow_outputs'])} workflow outputs")
        print(f"📄 Created {len(results['final_deliverables'])} final deliverables")
    else:
        print(f"❌ Workflow failed: {results['error']}")
    
    return results


def example_individual_agents():
    """Example: Use individual agents for specific tasks."""
    print("\\n" + "="*60)
    print("EXAMPLE 2: Individual Agent Usage")
    print("="*60)
    
    # Research Agent Example
    print("\\n🔍 Research Agent Example:")
    research_agent = ResearchAgent()
    research_result = research_agent.research_topic("Blockchain Technology", depth="focused")
    print("Research completed ✅")
    
    # Content Strategist Example  
    print("\\n📋 Content Strategist Example:")
    strategist = ContentStrategistAgent()
    strategy_result = strategist.create_content_strategy(
        topic="Blockchain Technology",
        research_insights=research_result,
        target_audience="technology executives"
    )
    print("Strategy developed ✅")
    
    # Writer Agent Example
    print("\\n✍️ Writer Agent Example:")
    writer = WriterAgent()
    content_result = writer.write_content(
        outline=strategy_result,
        requirements="Create a 1500-word article with professional tone",
        research_data=research_result
    )
    print("Content written ✅")
    
    # Editor Agent Example
    print("\\n📖 Editor Agent Example:")
    editor = EditorAgent()
    review_result = editor.comprehensive_review(
        content=content_result,
        requirements="Professional article for technology executives",
        seo_keywords=["blockchain", "technology", "business"]
    )
    print("Editorial review completed ✅")
    
    return {
        "research": research_result,
        "strategy": strategy_result, 
        "content": content_result,
        "review": review_result
    }


def example_collaborative_session():
    """Example: Collaborative agent session."""
    print("\\n" + "="*60)
    print("EXAMPLE 3: Collaborative Agent Session")
    print("="*60)
    
    workflow = ContentCreationWorkflow()
    
    # Run collaborative session on a specific challenge
    response = workflow.run_collaborative_session(
        topic="Artificial Intelligence Ethics",
        specific_challenge="How can we explain complex AI ethics concepts to a general business audience while maintaining accuracy and engaging readability?"
    )
    
    print("🤝 Collaborative session completed!")
    print("Team provided comprehensive solution ✅")
    
    return response


def example_custom_workflow():
    """Example: Create a custom workflow variation."""
    print("\\n" + "="*60)
    print("EXAMPLE 4: Custom Workflow Variation")
    print("="*60)
    
    # Initialize individual agents
    research_agent = ResearchAgent()
    strategist = ContentStrategistAgent()
    writer = WriterAgent()
    editor = EditorAgent()
    pm = ProjectManagerAgent()
    
    topic = "Quantum Computing Applications"
    
    print("🚀 Starting custom workflow...")
    
    # Step 1: Project planning
    project_init = pm.initiate_project(
        project_name=f"Custom Content: {topic}",
        client_requirements="Create educational content about quantum computing for business leaders"
    )
    print("1. Project initialized ✅")
    
    # Step 2: Parallel research and strategy
    print("2. Running research and initial strategy in parallel...")
    research_results = research_agent.research_topic(topic)
    
    # Step 3: Refine strategy based on research
    refined_strategy = strategist.create_content_strategy(
        topic=topic,
        research_insights=research_results,
        target_audience="business executives and decision makers"
    )
    print("3. Strategy refined based on research ✅")
    
    # Step 4: Content creation with quality check
    initial_content = writer.write_content(
        outline=refined_strategy,
        requirements="Educational, accessible tone for business audience",
        research_data=research_results
    )
    print("4. Initial content created ✅")
    
    # Step 5: Editorial review and final approval
    final_review = editor.final_quality_check(
        content=initial_content,
        original_requirements="Educational content for business executives"
    )
    print("5. Final quality check completed ✅")
    
    # Step 6: Project completion
    completion = pm.handle_project_completion(
        project_id="CUSTOM-001",
        final_deliverables=["Educational article on quantum computing", "Research summary", "Strategy document"]
    )
    print("6. Project completed ✅")
    
    return {
        "project_init": project_init,
        "research": research_results,
        "strategy": refined_strategy,
        "content": initial_content,
        "review": final_review,
        "completion": completion
    }


def main():
    """Run all examples."""
    print("🤖 AGNO MULTI-AGENT SYSTEM - USAGE EXAMPLES")
    print("="*80)
    
    try:
        # Example 1: Complete workflow
        workflow_results = example_complete_workflow()
        
        # Example 2: Individual agents
        individual_results = example_individual_agents()
        
        # Example 3: Collaborative session
        collaborative_results = example_collaborative_session()
        
        # Example 4: Custom workflow
        custom_results = example_custom_workflow()
        
        print("\\n" + "="*80)
        print("🎉 ALL EXAMPLES COMPLETED SUCCESSFULLY!")
        print("="*80)
        print("\\n📋 Summary:")
        print("✅ Complete workflow example")
        print("✅ Individual agent usage examples") 
        print("✅ Collaborative session example")
        print("✅ Custom workflow variation example")
        
        print("\\n💡 Next steps:")
        print("- Modify the examples for your specific use cases")  
        print("- Extend agents with additional capabilities")
        print("- Create new workflow patterns")
        print("- Add custom tools for your domain")
        
    except Exception as e:
        print(f"\\n❌ Example execution failed: {str(e)}")
        print("\\n🔧 Troubleshooting:")
        print("- Ensure you have set up API keys in .env file")
        print("- Check that all dependencies are installed")
        print("- Verify Python path includes the demo directory")


if __name__ == "__main__":
    main()