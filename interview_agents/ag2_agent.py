"""Interview agents for message processing."""

from google.adk.agents import Agent

def create_agent():
    """Create and return the interview message agent."""
    return Agent(
        name="interview_message_agent",
        description="An agent that processes and shortens messages",
        instruction="You are a helpful assistant that shortens messages while preserving their meaning.",
        model="gemini-2.5-pro"
    )

# Create a simple class that can be instantiated for backwards compatibility
class SimpleAgent:
    """A simple agent wrapper for the ADK agent."""
    
    def __init__(self):
        self.agent = create_agent()
        self.name = self.agent.name
        self.description = self.agent.description
    
    def query(self, input_data: str) -> str:
        """Process the input message using the ADK agent."""
        return str(self.agent.query(input_data))
    
    def __call__(self, input_data):
        """Make the class callable."""
        return self.query(input_data)