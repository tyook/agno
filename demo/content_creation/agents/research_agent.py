"""Research Agent for gathering information and insights."""

from agno.agent import Agent
from agno.models.anthropic import Claude
from demo.content_creation.tools.research_tools import web_search_tool, trend_analysis_tool, fact_check_tool
from demo.models.ai_model import sonnet_4, openai_gpt_4

class ResearchAgent:
    """Agent specialized in research and information gathering."""
    
    def __init__(self, model=None):
        self.model = openai_gpt_4
        
        self.agent = Agent(
            name="Research Agent",
            role="Information Researcher and Analyst",
            model=self.model,
            tools=[
                web_search_tool,
                trend_analysis_tool,
                fact_check_tool
            ],
            instructions="""
            You are a specialized Research Agent focused on gathering comprehensive and accurate information.
            
            Your responsibilities:
            1. Conduct thorough research on assigned topics
            2. Analyze trends and market data to provide insights
            3. Fact-check information and verify claims
            4. Provide well-sourced and reliable information
            5. Identify key themes, patterns, and emerging trends
            
            When conducting research:
            - Use multiple sources to verify information
            - Look for recent and authoritative sources
            - Identify both opportunities and challenges related to the topic
            - Provide context and background information
            - Highlight any conflicting information or uncertainties
            
            Always present your findings in a clear, organized manner with:
            - Key findings summary
            - Supporting evidence and sources
            - Trend analysis and implications
            - Recommendations for further investigation if needed
            
            Be thorough but concise, focusing on actionable insights.
            """,
            show_tool_calls=True,
            debug_mode=False
        )
    
    def research_topic(self, topic: str, depth: str = "comprehensive") -> str:
        """Research a specific topic."""
        prompt = f"""
        Please conduct {depth} research on the topic: "{topic}"
        
        I need you to:
        1. Search for current information and trends about this topic
        2. Analyze the trend data to understand market dynamics
        3. Fact-check key claims and statistics you find
        4. Provide a comprehensive research report with your findings
        
        Focus on providing actionable insights that would be valuable for content creation.
        """
        
        return self.agent.run(prompt)
    
    def verify_information(self, claims: list, context: str) -> str:
        """Verify specific claims or information."""
        prompt = f"""
        Please verify the following claims in the context of "{context}":
        
        Claims to verify:
        {chr(10).join(f"- {claim}" for claim in claims)}
        
        For each claim, use the fact-checking tool to verify accuracy and provide confidence levels.
        Summarize your findings and highlight any claims that need additional verification.
        """
        
        return self.agent.run(prompt)
    
    def analyze_competitive_landscape(self, topic: str, competitors: list = None) -> str:
        """Analyze the competitive landscape for a topic."""
        competitors_text = ""
        if competitors:
            competitors_text = f"Pay special attention to these competitors: {', '.join(competitors)}"
        
        prompt = f"""
        Analyze the competitive landscape for "{topic}".
        
        {competitors_text}
        
        Please research:
        1. Current market trends and opportunities
        2. Key players and their approaches
        3. Gaps in the market that could be addressed
        4. Emerging trends and future outlook
        
        Provide strategic insights that could inform content strategy and positioning.
        """
        
        return self.agent.run(prompt)