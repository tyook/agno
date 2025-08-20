"""Writer Agent for creating engaging content."""

from agno.agent import Agent
from agno.models.anthropic import Claude
from demo.content_creation.tools.content_tools import writing_quality_tool
from demo.models.ai_model import sonnet_4, openai_gpt_4

class WriterAgent:
    """Agent specialized in content writing and creation."""
    
    def __init__(self, model=None):
        self.model = openai_gpt_4
        
        self.agent = Agent(
            name="Writer Agent",
            role="Content Writer and Creator",
            model=self.model,
            tools=[
                writing_quality_tool
            ],
            instructions="""
            You are a skilled Writer Agent focused on creating engaging, high-quality content.
            
            Your responsibilities:
            1. Write compelling and well-structured content based on provided outlines
            2. Adapt tone and style to match target audience and brand requirements
            3. Ensure content is engaging, informative, and actionable
            4. Optimize content for readability and user experience
            5. Incorporate SEO requirements naturally into the writing
            6. Create strong headlines, introductions, and calls-to-action
            
            Writing best practices:
            - Start with compelling hooks that grab attention
            - Use clear structure with logical flow between sections
            - Include specific examples, case studies, and actionable insights
            - Write in an accessible yet professional tone
            - Use active voice and clear, concise language
            - Include relevant data and statistics to support points
            - End with strong conclusions and clear next steps
            
            Quality standards:
            - Content should be original and plagiarism-free
            - Information should be accurate and well-researched
            - Writing should be grammatically correct and well-edited
            - Content should provide real value to readers
            - SEO requirements should be naturally integrated
            
            Always use the writing quality tool to assess your content before finalizing.
            """,
            show_tool_calls=True,
            debug_mode=False
        )
    
    def write_content(self, outline: str, requirements: str, research_data: str = "") -> str:
        """Write content based on outline and requirements."""
        prompt = f"""
        Please write content based on the following specifications:
        
        Content Outline:
        {outline}
        
        Requirements:
        {requirements}
        
        Research Data (for reference):
        {research_data}
        
        Please create engaging, well-structured content that follows the outline and meets all requirements.
        After writing, use the writing quality tool to assess the content and make any necessary improvements.
        
        Focus on creating content that is:
        - Engaging and valuable to readers
        - Well-structured and easy to follow
        - Professional yet accessible in tone
        - Optimized for the specified reading level
        - Incorporating research insights naturally
        """
        
        return self.agent.run(prompt)
    
    def improve_readability(self, content: str, target_grade_level: int = 8) -> str:
        """Improve content readability."""
        prompt = f"""
        Please analyze and improve the readability of this content for a grade {target_grade_level} reading level:
        
        Content:
        {content}
        
        Use the writing quality tool to assess the current readability, then rewrite sections as needed to:
        1. Simplify complex sentences
        2. Use more accessible vocabulary where appropriate
        3. Improve paragraph structure and flow
        4. Add transitions and clarifying statements
        5. Ensure consistent tone throughout
        
        Maintain the core message and value while making it more accessible.
        """
        
        return self.agent.run(prompt)
    
    def create_compelling_introduction(self, topic: str, target_audience: str, key_benefits: list) -> str:
        """Create an engaging introduction for content."""
        prompt = f"""
        Create a compelling introduction for content about "{topic}" targeting {target_audience}.
        
        Key benefits to highlight:
        {chr(10).join(f"- {benefit}" for benefit in key_benefits)}
        
        The introduction should:
        1. Hook the reader with an interesting opening
        2. Clearly state what the content will cover
        3. Explain why it's valuable to the target audience
        4. Set expectations for what readers will learn
        5. Be approximately 150-200 words
        
        Make it engaging and compelling while staying professional.
        """
        
        return self.agent.run(prompt)
    
    def write_call_to_action(self, content_topic: str, desired_action: str, audience: str) -> str:
        """Create an effective call-to-action."""
        prompt = f"""
        Create an effective call-to-action for content about "{content_topic}".
        
        Desired Action: {desired_action}
        Target Audience: {audience}
        
        The CTA should:
        1. Be clear and specific about the next step
        2. Create urgency or motivation to act
        3. Be relevant to the content and audience
        4. Include compelling benefit-focused language
        5. Be approximately 50-100 words
        
        Make it persuasive but not pushy, focusing on value to the reader.
        """
        
        return self.agent.run(prompt)
    
    def adapt_tone_and_style(self, content: str, target_tone: str, brand_voice: str = "") -> str:
        """Adapt content tone and style to match requirements."""
        brand_context = f"Brand Voice Guidelines: {brand_voice}" if brand_voice else ""
        
        prompt = f"""
        Please adapt the tone and style of this content to match the specified requirements:
        
        Target Tone: {target_tone}
        {brand_context}
        
        Original Content:
        {content}
        
        Rewrite the content to match the target tone while maintaining:
        - The core message and information
        - Logical structure and flow
        - Key points and insights
        - SEO requirements
        
        Use the writing quality tool to ensure the adapted content maintains high quality standards.
        """
        
        return self.agent.run(prompt)