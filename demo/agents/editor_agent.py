"""Editor Agent for reviewing and refining content."""

from agno.agent import Agent
from agno.models.anthropic import Claude
from demo.tools.content_tools import writing_quality_tool, seo_optimizer_tool
from demo.tools.research_tools import fact_check_tool
from demo.models.ai_model import sonnet_4

class EditorAgent:
    """Agent specialized in content editing and quality assurance."""
    
    def __init__(self, model=None):
        self.model = sonnet_4
        
        self.agent = Agent(
            name="Editor Agent",
            role="Content Editor and Quality Assurance Specialist",
            model=self.model,
            tools=[
                writing_quality_tool,
                seo_optimizer_tool,
                fact_check_tool
            ],
            instructions="""
            You are an experienced Editor Agent focused on ensuring content quality and accuracy.
            
            Your responsibilities:
            1. Review content for grammar, style, and clarity
            2. Ensure factual accuracy and verify claims
            3. Optimize content structure and flow
            4. Check SEO compliance and optimization
            5. Maintain consistency in tone and messaging
            6. Ensure content meets quality standards and requirements
            
            Editing approach:
            - Thorough review for grammar, spelling, and punctuation
            - Fact-checking of claims, statistics, and assertions
            - Assessment of logical flow and argument structure
            - Optimization for readability and user experience
            - SEO compliance without compromising readability
            - Consistency check across all content elements
            
            Quality standards:
            - Content must be accurate and well-sourced
            - Writing should be clear, engaging, and error-free
            - Structure should be logical and easy to follow
            - SEO requirements should be naturally integrated
            - Tone should be consistent with brand guidelines
            - All claims should be verifiable and credible
            
            Always provide specific feedback and actionable recommendations for improvement.
            """,
            show_tool_calls=True,
            debug_mode=False
        )
    
    def comprehensive_review(self, content: str, requirements: str, seo_keywords: list = None) -> str:
        """Perform comprehensive content review."""
        if seo_keywords is None:
            seo_keywords = []
        
        primary_keyword = seo_keywords[0] if seo_keywords else ""
        secondary_keywords = seo_keywords[1:] if len(seo_keywords) > 1 else []
        
        prompt = f"""
        Please perform a comprehensive review of this content:
        
        Content Requirements:
        {requirements}
        
        SEO Keywords: {', '.join(seo_keywords) if seo_keywords else 'None specified'}
        
        Content to Review:
        {content}
        
        Please conduct a thorough review covering:
        1. Writing quality and readability assessment
        2. SEO optimization analysis (if keywords provided)
        3. Fact-checking of key claims and statistics
        4. Grammar, style, and consistency review
        5. Structure and flow evaluation
        6. Compliance with stated requirements
        
        Provide specific feedback and recommendations for improvement.
        """
        
        return self.agent.run(prompt)
    
    def fact_check_content(self, content: str, topic_context: str) -> str:
        """Fact-check content for accuracy."""
        prompt = f"""
        Please fact-check this content about "{topic_context}" for accuracy and credibility:
        
        Content:
        {content}
        
        Focus on:
        1. Verifying statistical claims and data points
        2. Checking factual assertions about the topic
        3. Identifying any outdated or potentially inaccurate information
        4. Assessing the credibility of claims made
        
        Use the fact-checking tool for key claims and provide a summary of verification results.
        Highlight any claims that need additional verification or correction.
        """
        
        return self.agent.run(prompt)
    
    def optimize_structure_and_flow(self, content: str) -> str:
        """Optimize content structure and logical flow."""
        prompt = f"""
        Please analyze and optimize the structure and flow of this content:
        
        Content:
        {content}
        
        Focus on:
        1. Logical progression of ideas and arguments
        2. Smooth transitions between sections
        3. Paragraph structure and coherence
        4. Overall narrative flow and readability
        5. Introduction and conclusion effectiveness
        
        Use the writing quality tool to assess current state and provide specific recommendations
        for structural improvements that would enhance reader experience.
        """
        
        return self.agent.run(prompt)
    
    def final_quality_check(self, content: str, original_requirements: str) -> str:
        """Perform final quality assurance check."""
        prompt = f"""
        Perform a final quality assurance check on this content:
        
        Original Requirements:
        {original_requirements}
        
        Final Content:
        {content}
        
        Verify that the content:
        1. Meets all original requirements and specifications
        2. Maintains high writing quality and readability
        3. Is factually accurate and well-supported
        4. Has proper SEO optimization (if applicable)
        5. Is ready for publication
        
        Provide a final assessment with:
        - Overall quality score
        - Compliance with requirements
        - Any remaining issues or recommendations
        - Publication readiness status
        
        Use all available tools to conduct this comprehensive final review.
        """
        
        return self.agent.run(prompt)
    
    def style_consistency_check(self, content: str, style_guide: str) -> str:
        """Check content for style consistency."""
        prompt = f"""
        Check this content for consistency with the provided style guidelines:
        
        Style Guidelines:
        {style_guide}
        
        Content:
        {content}
        
        Review for:
        1. Tone and voice consistency
        2. Formatting and structure compliance
        3. Terminology and language usage
        4. Brand voice adherence
        5. Style guide requirement compliance
        
        Identify any inconsistencies and provide specific recommendations for alignment.
        """
        
        return self.agent.run(prompt)