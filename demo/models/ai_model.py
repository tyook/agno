# Shared AI model configurations for all demo projects

from agno.models.aws.claude import Claude
from agno.models.openai import OpenAIChat
import os

"""
These are shared model definitions for use across all agno demo projects.
This centralizes the model configurations to make it easier to:
- Update model versions across all demos
- Add new models or modalities 
- Manage licensing changes consistently
"""

sonnet_4 = Claude(
    id="us.anthropic.claude-sonnet-4-20250514-v1:0",
    aws_access_key=os.getenv("AWS_BEDROCK_ACCESS_KEY_ID"),
    aws_secret_key=os.getenv("AWS_BEDROCK_SECRET_ACCESS_KEY"),
    aws_region="us-east-1",
)

# Set up default headers only if the environment variable is set
default_header_value = os.getenv("OPENAI_DEFAULT_HEADER")
headers = {"User-Id": default_header_value} if default_header_value else {}

openai_gpt_4 = OpenAIChat(
    id="gpt-4.1",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://openai-proxy.carta.team/v1",
    default_headers=headers,
)