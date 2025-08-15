"""Content Strategist Agent for planning content strategy."""

from agno.agent import Agent
from agno.models.anthropic import Claude
from demo.tools.content_tools import content_planner_tool, seo_optimizer_tool
from demo.models.ai_model import sonnet_4


class ContentStrategistAgent:
    """Agent specialized in content strategy and planning."""
    
    def __init__(self, model=None):
        self.model = sonnet_4
        
        self.agent = Agent(
            name="Content Strategist",
            role="Content Strategy and Planning Specialist",
            model=self.model,
            tools=[
                content_planner_tool,
                seo_optimizer_tool
            ],
            instructions="""
            You are a Content Strategist Agent focused on developing effective content strategies.
            
            Your responsibilities:
            1. Develop comprehensive content strategies based on research insights
            2. Create detailed content outlines and structures
            3. Define target audiences and messaging approaches
            4. Optimize content for SEO and discoverability
            5. Plan content calendars and publication schedules
            6. Ensure content aligns with business objectives
            
            When creating content strategies:
            - Consider the target audience's needs, preferences, and pain points
            - Align content goals with business objectives
            - Optimize for search engines while maintaining readability
            - Plan for different content formats and distribution channels
            - Include clear calls-to-action and conversion opportunities
            - Consider content lifecycle and updating needs
            
            Your deliverables should include:
            - Content outlines with clear structure
            - SEO keyword strategies
            - Target audience definitions
            - Content format recommendations
            - Success metrics and KPIs
            
            Be strategic and data-driven in your approach.
            """,
            show_tool_calls=True,
            debug_mode=False
        )
    
    def create_content_strategy(self, topic: str, research_insights: str, target_audience: str = "general") -> str:
        """Create a comprehensive content strategy."""
        prompt = f"""
        Based on the following research insights, create a comprehensive content strategy for "{topic}":
        
        Research Insights:
        {research_insights}
        
        Target Audience: {target_audience}
        
        Please develop:
        1. A detailed content plan with structure and outline
        2. SEO strategy including keyword recommendations
        3. Content format recommendations (blog post, article, etc.)
        4. Key messaging and positioning strategy
        5. Success metrics and KPIs to track
        
        Use the content planning and SEO optimization tools to create a well-structured strategy.
        """
        
        return self.agent.run(prompt)
    
    def optimize_for_seo(self, content_draft: str, primary_keyword: str, secondary_keywords: list = None) -> str:
        """Optimize content for SEO."""
        if secondary_keywords is None:
            secondary_keywords = []
        
        prompt = f"""
        Please analyze and optimize the following content for SEO:
        
        Primary Keyword: {primary_keyword}
        Secondary Keywords: {', '.join(secondary_keywords) if secondary_keywords else 'None specified'}
        
        Content Draft:
        {content_draft}
        
        Use the SEO optimizer tool to analyze the content and provide specific recommendations for improvement.
        Include suggestions for meta titles, descriptions, and keyword optimization.
        """
        
        return self.agent.run(prompt)
    
    def plan_content_series(self, main_topic: str, research_data: str, num_pieces: int = 3) -> str:
        """Plan a series of related content pieces."""
        prompt = f"""
        Based on the research data about "{main_topic}", plan a series of {num_pieces} related content pieces.
        
        Research Data:
        {research_data}
        
        For each content piece, provide:
        1. Specific topic/angle
        2. Content type and format
        3. Target audience segment
        4. Key messaging points
        5. SEO considerations
        
        Ensure the series covers different aspects of the main topic and appeals to various audience segments.
        Use the content planner tool for each piece in the series.
        """
        
        return self.agent.run(prompt)
    
    def define_content_requirements(self, strategy: str) -> str:
        """Define specific requirements for content creation."""
        prompt = f"""
        Based on this content strategy, define specific requirements for the writing team:
        
        Strategy:
        {strategy}
        
        Please specify:
        1. Tone and style guidelines
        2. Word count and structure requirements
        3. Key points that must be covered
        4. SEO requirements and keyword usage
        5. Call-to-action specifications
        6. Quality standards and success criteria
        
        Make the requirements clear and actionable for the writing team.
        """
        
        return self.agent.run(prompt)