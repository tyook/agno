#!/usr/bin/env python3
"""
Test script to verify agno 1.7.6 imports work correctly.
Run this to check if all imports are working before running the main demo.
"""

import sys
import os

def test_agno_imports():
    """Test if all agno imports work correctly."""
    print("🧪 Testing agno v1.7.6 imports...")
    
    try:
        # Test core agno imports
        print("  Importing core agno components...")
        from agno.agent import Agent
        from agno.team import Team
        print("  ✅ Core components imported successfully")
        
        # Test model imports
        print("  Importing model components...")
        from agno.models.anthropic import Claude
        print("  ✅ Model components imported successfully")
        
        # Test agent initialization
        print("  Testing agent initialization...")
        model = Claude(id="claude-3-5-sonnet-20241022")
        agent = Agent(
            name="Test Agent",
            model=model,
            instructions="You are a test agent."
        )
        print("  ✅ Agent initialized successfully")
        
        # Test tool creation
        print("  Testing tool creation...")
        from agno.tools import tool
        
        @tool(
            name="test_tool",
            description="A simple test tool"
        )
        def test_tool_func(test_param: str = "test") -> dict:
            return {"result": f"Tool executed with param: {test_param}"}
        
        print("  ✅ Custom tool created successfully")
        
        # Test team creation
        print("  Testing team creation...")
        team = Team(members=[agent])
        print("  ✅ Team created successfully")
        
        print("\\n🎉 All agno v1.7.6 imports and initialization tests passed!")
        return True
        
    except ImportError as e:
        print(f"  ❌ Import error: {e}")
        print("\\n💡 Make sure agno v1.7.6 is installed:")
        print("    pip install agno==1.7.6")
        return False
        
    except Exception as e:
        print(f"  ❌ Initialization error: {e}")
        print("\\n💡 There might be API changes in agno v1.7.6")
        print("    Check the agno documentation for the correct API usage")
        return False


def main():
    """Run all import tests."""
    print("🚀 AGNO v1.7.6 COMPATIBILITY TEST")
    print("=" * 50)
    
    # Test agno imports
    agno_success = test_agno_imports()
    
    
    print("\\n" + "=" * 50)
    if agno_success:
        print("✅ ALL TESTS PASSED - Demo is ready to run!")
        print("\\n🎮 You can now run the demo:")
        print("    python demo.py")
    else:
        print("❌ SOME TESTS FAILED - Please fix issues before running demo")
        if not agno_success:
            print("  - Fix agno installation/import issues")


if __name__ == "__main__":
    main()