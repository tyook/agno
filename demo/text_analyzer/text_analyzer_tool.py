"""Simple text analyzer agent that returns structured output."""

from typing import List, Dict, Any
from pydantic import BaseModel, Field
from agno.agent import Agent
from agno.models.anthropic import Claude
from demo.models.ai_model import sonnet_4, openai_gpt_4
from demo.text_analyzer.tools import review_fetch_tool

class Review(BaseModel):
    """Complete text analysis results."""
    word_count: int = Field(..., description="Total number of words")
    sentence_count: int = Field(..., description="Total number of sentences")
    reading_level: str = Field(..., description="Estimated reading level (elementary, middle, high school, college)")
    
    # Flattened sentiment fields
    sentiment_positive: float = Field(..., description="Positive sentiment score (0-1)")
    sentiment_negative: float = Field(..., description="Negative sentiment score (0-1)")
    sentiment_neutral: float = Field(..., description="Neutral sentiment score (0-1)")
    sentiment_overall: str = Field(..., description="Overall sentiment: positive, negative, or neutral")
    
    # Instead of nested key_topics, we'll use a simpler structure
    topics: List[str] = Field(..., description="List of key topics identified in the text")
    topic_relevance: List[float] = Field(..., description="Relevance scores for each topic (0-1)")
    topic_keywords: List[List[str]] = Field(..., description="Keywords for each topic")
    
    summary: str = Field(..., description="Brief summary of the text")
    main_points: List[str] = Field(..., description="Main points from the text")


class ReviewList(BaseModel):
    """Complete text analysis results."""
    reviews: List[Review] = Field(..., description="reviews")


class TextAnalyzerWithToolAgent:
    """Simple agent that analyzes text and returns structured output."""
    
    def __init__(self):
        """Initialize the text analyzer agent."""
        self.model = openai_gpt_4
        
        self.agent = Agent(
            name="Text Analyzer",
            role="Text Analysis Specialist", 
            model=self.model,
            instructions="""
            You are a product review analysis specialist. Your job is to analyze product reviews and provide comprehensive insights.

            # First, you need to fetch review using review_fetch_tool.
            
            For every review you analyze, provide:
            1. Basic statistics (word count, sentence count)
            2. Reading level assessment
            3. Sentiment analysis with detailed scores (positive, negative, neutral scores from 0-1, and overall sentiment)
            4. Key topics as a list, with separate lists for relevance scores and keywords for each topic
            5. A concise summary
            6. Main points extracted from the text
            
            Be accurate, thorough, and provide specific numerical scores where requested.
            Your analysis should be objective and data-driven.
            
            IMPORTANT: Format your response to match the TextAnalysis schema exactly:
            - sentiment_positive, sentiment_negative, sentiment_neutral: Float values between 0-1
            - sentiment_overall: String ("positive", "negative", or "neutral")
            - topics: List of topic strings
            - topic_relevance: List of float values (0-1) corresponding to each topic
            - topic_keywords: List of lists, where each inner list contains keywords for a topic
            """,
            show_tool_calls=False,
            debug_mode=False,
            response_model=ReviewList,
            tools=[review_fetch_tool]
        )

    

def demo_text_analyzer_with_tool():
    """Demonstrate the text analyzer with sample text."""
    analyzer = TextAnalyzerWithToolAgent()
    
    
    print("🔍 TEXT ANALYZER DEMO - Structured Output With Tool Example")
    print("=" * 60)

    response = analyzer.agent.run()

    
    for i, sample in enumerate(response.content.reviews, 1):

        
        try:
            
            # Display results
            print(f"\n📊 ANALYSIS RESULTS:")

            print(f"Word Count: {sample.word_count}")
            print(f"Sentence Count: {sample.sentence_count}")
            print(f"Reading Level: {sample.reading_level}")
            
            print(f"\n💭 SENTIMENT:")
            print(f"  Overall: {sample.sentiment_overall}")
            print(f"  Positive: {sample.sentiment_positive:.2f}")
            print(f"  Negative: {sample.sentiment_negative:.2f}")
            print(f"  Neutral: {sample.sentiment_neutral:.2f}")
            
            print(f"\n🎯 KEY TOPICS:")
            for i, topic in enumerate(sample.topics):
                # Access relevance and keywords using the same index
                relevance = sample.topic_relevance[i]
                keywords = sample.topic_keywords[i]
                print(f"  • {topic} (relevance: {relevance:.2f})")
                print(f"    Keywords: {', '.join(keywords)}")
            
            print(f"\n📝 SUMMARY:")
            print(f"  {sample.summary}")
            
            print(f"\n🔑 MAIN POINTS:")
            for j, point in enumerate(sample.main_points, 1):
                print(f"  {j}. {point}")
                
        except Exception as e:
            print(f"❌ Analysis failed: {e}")
        


if __name__ == "__main__":
    demo_text_analyzer_with_tool()