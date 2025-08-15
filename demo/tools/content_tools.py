"""Content creation and analysis tools."""

import json
import re
from typing import Dict, List, Any
from agno.tools import tool


@tool(
    name="content_planner",
    description="Create content plans and outlines for topics",
)
def content_planner_tool(topic: str, content_type: str = "blog_post", target_audience: str = "general") -> Dict[str, Any]:
    """
    Create content plans and outlines for topics.
    
    Args:
        topic: Main topic for content
        content_type: Type of content (blog_post, article, social_media)
        target_audience: Target audience description
        
    Returns:
        Dictionary with content plan details
    """
    # Generate content outline based on type
    if content_type == "blog_post":
        outline = [
            "Introduction - Hook and overview",
            f"What is {topic}? - Definition and context",
            f"Key benefits/applications of {topic}",
            f"Current trends in {topic}",
            f"Challenges and considerations",
            f"Future outlook for {topic}",
            "Conclusion and call-to-action"
        ]
        word_count = "1500-2000 words"
    elif content_type == "article":
        outline = [
            "Executive summary",
            f"Background on {topic}",
            "Detailed analysis",
            "Case studies and examples",
            "Expert insights",
            "Implications and recommendations"
        ]
        word_count = "2500-3500 words"
    else:  # social_media
        outline = [
            "Attention-grabbing opening",
            f"Key point about {topic}",
            "Call-to-action or question"
        ]
        word_count = "100-280 characters"
    
    return {
        "topic": topic,
        "content_type": content_type,
        "target_audience": target_audience,
        "outline": outline,
        "recommended_word_count": word_count,
        "seo_keywords": [topic.lower(), f"{topic} guide", f"{topic} tips", f"{topic} benefits"],
        "tone": "professional yet accessible",
        "estimated_reading_time": "8-12 minutes" if content_type == "blog_post" else "15-20 minutes"
    }


@tool(
    name="writing_quality",
    description="Analyze writing quality, readability, and style",
)
def writing_quality_tool(text: str, target_grade_level: int = 8) -> Dict[str, Any]:
    """
    Analyze writing quality, readability, and style.
    
    Args:
        text: Text content to analyze
        target_grade_level: Target reading grade level
        
    Returns:
        Dictionary with quality analysis results
    """
    # Basic text analysis
    word_count = len(text.split())
    sentence_count = len([s for s in text.split('.') if s.strip()])
    paragraph_count = len([p for p in text.split('\n\n') if p.strip()])
    
    # Simulate readability metrics
    avg_sentence_length = word_count / max(sentence_count, 1)
    readability_score = max(1, min(12, 15 - (avg_sentence_length * 0.5)))
    
    # Quality indicators
    quality_score = 0.8 if word_count > 100 else 0.6
    
    issues = []
    if avg_sentence_length > 25:
        issues.append("Some sentences are too long - consider breaking them up")
    if word_count < 300:
        issues.append("Content might be too brief for the topic")
    
    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "paragraph_count": paragraph_count,
        "avg_sentence_length": round(avg_sentence_length, 1),
        "readability_grade_level": round(readability_score, 1),
        "quality_score": quality_score,
        "issues_found": issues,
        "recommendations": [
            "Add more specific examples and case studies",
            "Include relevant statistics and data",
            "Ensure smooth transitions between paragraphs"
        ]
    }


@tool(
    name="seo_optimizer",
    description="Analyze content for SEO optimization opportunities",
)
def seo_optimizer_tool(content: str, primary_keyword: str, secondary_keywords: List[str] = None) -> Dict[str, Any]:
    """
    Analyze content for SEO optimization opportunities.
    
    Args:
        content: Content to analyze for SEO
        primary_keyword: Primary keyword to optimize for
        secondary_keywords: Secondary keywords list
        
    Returns:
        Dictionary with SEO analysis and suggestions
    """
    if secondary_keywords is None:
        secondary_keywords = []
    
    content_lower = content.lower()
    primary_count = content_lower.count(primary_keyword.lower())
    word_count = len(content.split())
    
    # Calculate keyword density
    keyword_density = (primary_count / word_count) * 100 if word_count > 0 else 0
    
    suggestions = []
    if keyword_density < 1:
        suggestions.append(f"Consider adding more instances of '{primary_keyword}' (current density: {keyword_density:.1f}%)")
    elif keyword_density > 3:
        suggestions.append(f"Keyword density is high ({keyword_density:.1f}%) - consider reducing to avoid over-optimization")
    
    if not any(kw.lower() in content_lower for kw in secondary_keywords):
        suggestions.append("Include some secondary keywords naturally in the content")
    
    return {
        "primary_keyword": primary_keyword,
        "keyword_density": round(keyword_density, 2),
        "secondary_keywords_found": [kw for kw in secondary_keywords if kw.lower() in content_lower],
        "seo_score": min(100, max(0, 70 + (primary_count * 5) - abs(keyword_density - 2) * 10)),
        "suggestions": suggestions,
        "meta_title_suggestion": f"{primary_keyword.title()}: Complete Guide and Best Practices",
        "meta_description_suggestion": f"Learn everything about {primary_keyword} including benefits, applications, and expert insights. Comprehensive guide for 2024."
    }