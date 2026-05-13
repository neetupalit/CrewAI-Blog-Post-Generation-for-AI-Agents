from crewai import Agent
from .tools import get_news # Import the custom tool

# Agent configurations (extracted from 4a-APgJer-Q0 and combined with NxSnSm7PqJs_)
researcher_base_config = {
  "role": "Research Analyst",
  "goal": "Find accurate information about {topic}",
  "backstory": "Expert AI researcher with 10 years of experience"
}

writer_base_config = {
  "role": "Technical Writer",
  "goal": "Write clear blog posts based on research",
  "backstory": "Senior content writer specializing in AI"
}

# Instantiate agents (combining h_x5L_3QsIgz and NxSnSm7PqJs_)
researcher = Agent(
    llm="groq/llama-3.3-70b-versatile", # LLM assumed based on previous cells
    tools=[get_news], # Include the custom tool
    verbose=True, # Enable verbose output for better debugging
    **researcher_base_config # Unpack the base config
)

writer = Agent(
    llm="groq/llama-3.3-70b-versatile", # LLM assumed based on previous cells
    verbose=True, # Enable verbose output
    **writer_base_config # Unpack the base config
)
