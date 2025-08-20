# AI model configuration for Team API demo

from agno.models.aws.claude import Claude
import os

"""
Model definitions for the Team API demo.
Using AWS Bedrock Claude for team collaboration.
"""

sonnet_4 = Claude(
    id="us.anthropic.claude-sonnet-4-20250514-v1:0",
    aws_access_key=os.getenv("AWS_BEDROCK_ACCESS_KEY_ID"),
    aws_secret_key=os.getenv("AWS_BEDROCK_SECRET_ACCESS_KEY"),
    aws_region="us-east-1",
)
