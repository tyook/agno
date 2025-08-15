#!/usr/bin/env python3
"""
Validation script to test that all tools work correctly with the new decorator pattern.
"""

import sys
import os

# Add the demo package to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_research_tools():
    """Test research tools work correctly."""
    print("🔍 Testing Research Tools...")
    
    try:
        from demo.tools.research_tools import web_search_tool, trend_analysis_tool, fact_check_tool
        
        # Test web search tool
        search_result = web_search_tool.entrypoint(query="AI in healthcare", num_results=3)
        assert "results" in search_result
        assert len(search_result["results"]) == 3
        print("  ✅ web_search_tool working")
        
        # Test trend analysis tool
        trend_result = trend_analysis_tool.entrypoint(topic="machine learning", timeframe="monthly")
        assert "trend_direction" in trend_result
        assert "growth_rate" in trend_result
        print("  ✅ trend_analysis_tool working")
        
        # Test fact check tool
        fact_result = fact_check_tool.entrypoint(claim="AI improves healthcare outcomes", topic_context="healthcare AI")
        assert "verification_status" in fact_result
        assert "confidence_score" in fact_result
        print("  ✅ fact_check_tool working")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Research tools error: {e}")
        return False


def test_content_tools():
    """Test content tools work correctly."""
    print("\\n📝 Testing Content Tools...")
    
    try:
        from demo.tools.content_tools import content_planner_tool, writing_quality_tool, seo_optimizer_tool
        
        # Test content planner tool
        plan_result = content_planner_tool.entrypoint(topic="blockchain", content_type="blog_post", target_audience="developers")
        assert "outline" in plan_result
        assert "seo_keywords" in plan_result
        print("  ✅ content_planner_tool working")
        
        # Test writing quality tool
        quality_result = writing_quality_tool.entrypoint(text="This is a sample text for testing. It has multiple sentences. The quality should be assessed.", target_grade_level=8)
        assert "word_count" in quality_result
        assert "readability_grade_level" in quality_result
        print("  ✅ writing_quality_tool working")
        
        # Test SEO optimizer tool
        seo_result = seo_optimizer_tool.entrypoint(content="Blockchain technology is revolutionizing finance. Blockchain offers security and transparency.", primary_keyword="blockchain", secondary_keywords=["technology", "finance"])
        assert "keyword_density" in seo_result
        assert "seo_score" in seo_result
        print("  ✅ seo_optimizer_tool working")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Content tools error: {e}")
        return False


def test_project_tools():
    """Test project management tools work correctly."""
    print("\\n🎯 Testing Project Tools...")
    
    try:
        from demo.tools.project_tools import task_manager_tool, progress_tracker_tool, communication_tool
        
        # Test task manager tool
        task_result = task_manager_tool.entrypoint(action="create", task_details={"title": "Test Task", "assignee": "test_agent"})
        assert task_result["status"] == "created"
        assert "task" in task_result
        print("  ✅ task_manager_tool working")
        
        # Test progress tracker tool
        progress_result = progress_tracker_tool.entrypoint(project_id="TEST-001", milestone="Initial setup", completion_percentage=25.0)
        assert "current_progress" in progress_result
        assert "next_steps" in progress_result
        print("  ✅ progress_tracker_tool working")
        
        # Test communication tool
        comm_result = communication_tool.entrypoint(recipient="team", message_type="update", content="Project status update", priority="medium")
        assert comm_result["status"] == "delivered"
        assert "message_id" in comm_result
        print("  ✅ communication_tool working")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Project tools error: {e}")
        return False


def test_agent_initialization():
    """Test that agents can be initialized with the new tools."""
    print("\\n🤖 Testing Agent Initialization...")
    
    try:
        # Test that we can import and initialize agents
        from demo.agents.research_agent import ResearchAgent
        from demo.agents.strategist_agent import ContentStrategistAgent
        from demo.agents.writer_agent import WriterAgent
        from demo.agents.editor_agent import EditorAgent
        from demo.agents.project_manager_agent import ProjectManagerAgent
        
        # Initialize each agent (this will test tool integration)
        research_agent = ResearchAgent()
        strategist_agent = ContentStrategistAgent()
        writer_agent = WriterAgent()
        editor_agent = EditorAgent()
        pm_agent = ProjectManagerAgent()
        
        print("  ✅ All agents initialized successfully")
        print("  ✅ Tool integration working")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Agent initialization error: {e}")
        return False


def main():
    """Run all validation tests."""
    print("🧪 AGNO TOOL VALIDATION TESTS")
    print("=" * 50)
    
    tests = [
        test_research_tools,
        test_content_tools, 
        test_project_tools,
        test_agent_initialization
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\\n" + "=" * 50)
    if all(results):
        print("🎉 ALL VALIDATION TESTS PASSED!")
        print("\\n✅ Tool decorator pattern is working correctly")
        print("✅ All tools are functional")
        print("✅ Agent integration is successful")
        print("✅ Demo is ready to run")
        
        print("\\n🚀 You can now run:")
        print("    python demo.py")
    else:
        print("❌ SOME VALIDATION TESTS FAILED")
        print("\\n🔧 Issues to fix:")
        for i, (test, result) in enumerate(zip(tests, results)):
            if not result:
                print(f"  - {test.__name__} failed")
        
        print("\\n💡 Check the error messages above for details")


if __name__ == "__main__":
    main()