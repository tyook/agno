"""Simple text analyzer agent that returns structured output."""

from typing import List, Dict, Any
from pydantic import BaseModel, Field
from agno.agent import Agent
from agno.models.anthropic import Claude
from demo.structured_output.models.ai_model import sonnet_4


class SentimentScore(BaseModel):
    """Sentiment analysis score."""
    positive: float = Field(..., description="Positive sentiment score (0-1)")
    negative: float = Field(..., description="Negative sentiment score (0-1)")
    neutral: float = Field(..., description="Neutral sentiment score (0-1)")
    overall: str = Field(..., description="Overall sentiment: positive, negative, or neutral")


class KeyTopic(BaseModel):
    """Key topic identified in the text."""
    topic: str = Field(..., description="The topic name")
    relevance: float = Field(..., description="Relevance score (0-1)")
    keywords: List[str] = Field(..., description="Keywords related to this topic")


class TextAnalysis(BaseModel):
    """Complete text analysis results."""
    word_count: int = Field(..., description="Total number of words")
    sentence_count: int = Field(..., description="Total number of sentences")
    reading_level: str = Field(..., description="Estimated reading level (elementary, middle, high school, college)")
    sentiment: SentimentScore = Field(..., description="Sentiment analysis")
    key_topics: List[KeyTopic] = Field(..., description="Key topics identified in the text")
    summary: str = Field(..., description="Brief summary of the text")
    main_points: List[str] = Field(..., description="Main points from the text")


class TextAnalyzerAgent:
    """Simple agent that analyzes text and returns structured output."""
    
    def __init__(self):
        """Initialize the text analyzer agent."""
        self.model = sonnet_4
        
        self.agent = Agent(
            name="Text Analyzer",
            role="Text Analysis Specialist", 
            model=self.model,
            instructions="""
            You are a text analysis specialist. Your job is to analyze any given text and provide comprehensive insights.
            
            For every text you analyze, provide:
            1. Basic statistics (word count, sentence count)
            2. Reading level assessment
            3. Sentiment analysis with detailed scores
            4. Key topics with relevance scores and keywords
            5. A concise summary
            6. Main points extracted from the text
            
            Be accurate, thorough, and provide specific numerical scores where requested.
            Your analysis should be objective and data-driven.
            """,
            show_tool_calls=False,
            debug_mode=False,
            response_model=TextAnalysis
        )
    
    def analyze_text(self, text: str) -> TextAnalysis:
        """
        Analyze the given text and return structured results.
        
        Args:
            text: The text to analyze
            
        Returns:
            TextAnalysis: Structured analysis results
        """
        prompt = f"""
        Please analyze the following text and provide a comprehensive analysis:

        TEXT TO ANALYZE:
        {text}

        Provide your analysis in the exact format specified by the TextAnalysis schema.
        Make sure all numerical scores are between 0 and 1, and be precise with your counts and assessments.
        """
        
        # Use the agent to generate structured output
        response = self.agent.run(
            prompt,
        )
        
        return response


def demo_text_analyzer():
    """Demonstrate the text analyzer with sample text."""
    analyzer = TextAnalyzerAgent()
    
    sample_texts = [
        {
            "title": "Product Review",
            "text": """
            I recently purchased this laptop and I'm extremely disappointed with the performance. 
            The battery life is terrible, lasting only 2 hours on a full charge. The screen quality 
            is subpar and the keyboard feels cheap. However, the design is sleek and it's lightweight. 
            Customer service was unhelpful when I contacted them about these issues. 
            I would not recommend this product to anyone looking for a reliable laptop.
            """
        },
        {
            "title": "Scientific Article Excerpt",
            "text": """
            Climate change represents one of the most significant challenges facing humanity in the 21st century. 
            Rising global temperatures, caused primarily by increased greenhouse gas emissions from human activities, 
            are leading to widespread environmental changes. These include melting polar ice caps, rising sea levels, 
            more frequent extreme weather events, and shifts in precipitation patterns. The Intergovernmental Panel 
            on Climate Change has documented these trends extensively, providing scientific evidence for the urgent 
            need for mitigation and adaptation strategies. Renewable energy technologies, carbon capture systems, 
            and sustainable development practices are essential components of the global response to this crisis.
            """
        }
    ]
    
    print("🔍 TEXT ANALYZER DEMO - Structured Output Example")
    print("=" * 60)
    
    for i, sample in enumerate(sample_texts, 1):
        print(f"\n📄 Example {i}: {sample['title']}")
        print("-" * 40)
        print(f"Text: {sample['text'][:100]}...")
        
        try:
            # Analyze the text
            analysis = analyzer.analyze_text(sample['text'])
            
            # Display results
            print(f"\n📊 ANALYSIS RESULTS:")
            
            print(f"Word Count: {analysis.content.word_count}")
            print(f"Sentence Count: {analysis.content.sentence_count}")
            print(f"Reading Level: {analysis.content.reading_level}")
            
            print(f"\n💭 SENTIMENT:")
            print(f"  Overall: {analysis.content.sentiment.overall}")
            print(f"  Positive: {analysis.content.sentiment.positive:.2f}")
            print(f"  Negative: {analysis.content.sentiment.negative:.2f}")
            print(f"  Neutral: {analysis.content.sentiment.neutral:.2f}")
            
            print(f"\n🎯 KEY TOPICS:")
            for topic in analysis.content.key_topics:
                print(f"  • {topic.topic} (relevance: {topic.relevance:.2f})")
                print(f"    Keywords: {', '.join(topic.keywords)}")
            
            print(f"\n📝 SUMMARY:")
            print(f"  {analysis.content.summary}")
            
            print(f"\n🔑 MAIN POINTS:")
            for j, point in enumerate(analysis.content.main_points, 1):
                print(f"  {j}. {point}")
                
        except Exception as e:
            print(f"❌ Analysis failed: {e}")
        
        if i < len(sample_texts):
            print("\n" + "=" * 60)


if __name__ == "__main__":
    demo_text_analyzer()