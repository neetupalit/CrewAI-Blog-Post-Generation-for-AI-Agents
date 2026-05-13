from crewai import Task
from pydantic import BaseModel
from .agents import researcher, writer # Import instantiated agents

# Pydantic model for structured output (from U42Sj-1sshGm)
class BlogOutput(BaseModel):
    title: str
    content: str
    word_count: int
    tags: list[str]

# Task definitions (combining -T9ShjEbrGdm, h_x5L_3QsIgz, and U42Sj-1sshGm)
research_task = Task(
  description="Research {topic} and find top developments",
  expected_output="Bullet list of 5 key findings",
  agent=researcher
)

write_task = Task(
  description="Write a blog post about AI agents", # Specific description for the default run
  expected_output="Structured blog post",
  agent=writer,
  output_pydantic=BlogOutput, # Use Pydantic for output validation and parsing
  context=[research_task] # Link the research task as context for the writer
)
