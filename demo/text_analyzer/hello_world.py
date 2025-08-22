"""Simple text analyzer agent that returns structured output."""

from typing import List, Dict, Any
from pydantic import BaseModel, Field
from agno.agent import Agent
from agno.models.anthropic import Claude
from demo.models.ai_model import sonnet_4, openai_gpt_4
from agno.memory.v2 import Memory

class HelloWorldAgent:
    """Simple agent that analyzes text and returns structured output."""
    
    def __init__(self):
        """Initialize the text analyzer agent."""
        self.model = openai_gpt_4
        
        self.agent = Agent(
            name="Hello World Agent",
            role="Saying hello",
            model=self.model,
            instructions="""
            You are a friendly conversational assistant. 
            
            Your responsibilities:
            1. Always start your responses with a warm greeting or acknowledgment
            2. Be helpful and engaging in your responses
            3. Remember and reference previous parts of our conversation when relevant
            4. Maintain a friendly and professional tone
            
            Format your responses to always include a greeting at the beginning, such as:
            - "Hello! [your response]"
            - "Hi there! [your response]" 
            - "Great question! [your response]"
            - "Thanks for asking! [your response]"
            """,
            show_tool_calls=True,
            debug_mode=False,
        )
class ConversationalAgent:
    """Simple agent that analyzes text and returns structured output."""
    
    def __init__(self):
        """Initialize the text analyzer agent."""
        self.model = openai_gpt_4
        
        self.agent = Agent(
            name="Conversational Agent",
            role="Friendly Assistant",
            model=self.model,
            instructions="""
            You are a friendly conversational assistant. 
            
            Your responsibilities:
            1. Always start your responses with a warm greeting or acknowledgment
            2. Be helpful and engaging in your responses
            3. Remember and reference previous parts of our conversation when relevant
            4. Maintain a friendly and professional tone
            
            Format your responses to always include a greeting at the beginning, such as:
            - "Hello! [your response]"
            - "Hi there! [your response]" 
            - "Great question! [your response]"
            - "Thanks for asking! [your response]"
            """,
            # Multi-user, multi-session only work with Memory.v2
            memory=Memory(),
            add_history_to_messages=True,
            num_history_runs=3,
        )
    

def hello_world():
    """Demonstrate the text analyzer with sample text."""
    
    convo_agent = ConversationalAgent().agent
    convo_agent = HelloWorldAgent().agent

    user_1_id = "user_101"
    

    user_1_session_id = "session_101"
    

    # # Start the session with user 1
    # convo_agent.print_response(
    #     "Tell me a 5 second short story about a robot.",
    #     user_id=user_1_id,
    #     session_id=user_1_session_id,
    # )
    # # Continue the session with user 1
    # convo_agent.print_response("Now tell me a joke.", user_id=user_1_id, session_id=user_1_session_id)




    
    while True:
        print("\n📝 Enter text to analyze:")
        user_text = input("> ")
        
        if user_text.lower() in ['quit', 'exit', 'q']:
            print("👋 Goodbye!")
            break
            
        if len(user_text.strip()) < 10:
            print("⚠️  Please enter at least 10 characters of text.")
            continue
        
        try:
            print("\n🔄 Analyzing...")
            # analysis = agent.analyze_text(user_text)
            # response = agent.agent.run(prompt=user_text)
            convo_agent.print_response(
                user_text,
            )

            # print(f"response: {response}")
            
                
        except Exception as e:
            print(f"❌ Analysis failed: {e}")


if __name__ == "__main__":
    hello_world()