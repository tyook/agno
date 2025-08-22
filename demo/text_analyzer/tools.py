"""PDF processing tools for bank statement analysis."""

import json
from typing import List, Dict, Any
from agno.tools import tool

from demo.text_analyzer.reviews import REVIEWS



@tool(
    name="review_fetch_tool",
    description="Fetches reviews of products.",
)
def review_fetch_tool() -> str:

    return REVIEWS


