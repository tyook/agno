#!/usr/bin/env python3
"""Validate that the Team API demo setup is working correctly."""

import os
import sys

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

def validate_imports():
    """Test that all required imports work."""
    try:
        from agno.team import Team
        from agno.agent import Agent
        from demo.team_api_demo.models.ai_model import sonnet_4
        print("✅ All imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def validate_model_config():
    """Test that the model configuration is accessible."""
    try:
        from demo.team_api_demo.models.ai_model import sonnet_4
        print(f"✅ Model configuration loaded: {sonnet_4.id}")
        return True
    except Exception as e:
        print(f"❌ Model configuration error: {e}")
        return False

def check_api_credentials():
    """Check if AWS credentials are set."""
    access_key = os.getenv("AWS_BEDROCK_ACCESS_KEY_ID")
    secret_key = os.getenv("AWS_BEDROCK_SECRET_ACCESS_KEY")
    
    if access_key and secret_key:
        print("✅ AWS credentials found")
        return True
    else:
        print("⚠️  AWS credentials not found (demo will require them to run)")
        print("   Set AWS_BEDROCK_ACCESS_KEY_ID and AWS_BEDROCK_SECRET_ACCESS_KEY")
        return False

def main():
    """Run all validation checks."""
    print("🔧 Team API Demo - Setup Validation")
    print("=" * 40)
    
    import_ok = validate_imports()
    model_ok = validate_model_config()
    creds_ok = check_api_credentials()
    
    print("\n📋 Summary:")
    if import_ok and model_ok:
        print("✅ Setup is ready for Team API demo")
        if not creds_ok:
            print("   (Add AWS credentials to run the full demo)")
    else:
        print("❌ Setup has issues that need to be resolved")
    
    return import_ok and model_ok

if __name__ == "__main__":
    main()