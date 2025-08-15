# Named the file ai_models instead of models intending to indicate that this is not a Django model file

from agno.models.aws.claude import Claude
import os
from django.conf import settings

"""
These are just client definitions for using with agno agents. If you find you want to use a different model, or you want
to add modalities, just add them here. Centralizing the definitions will make it easier to find old models that should 
be updated, or to find usages of models that we might lose access to as licensing changes.
"""

sonnet_4 = Claude(
    id="us.anthropic.claude-sonnet-4-20250514-v1:0",
    aws_access_key=os.getenv("AWS_BEDROCK_ACCESS_KEY_ID"),
    aws_secret_key=os.getenv("AWS_BEDROCK_SECRET_ACCESS_KEY"),
    aws_region="us-east-1",
)
