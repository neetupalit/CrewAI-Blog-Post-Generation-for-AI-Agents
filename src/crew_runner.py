import os
from crewai import Crew, Process

# Import agents and tasks from modularized files
from .agents import researcher, writer
from .tasks import research_task, write_task, BlogOutput

# Set GROQ_API_KEY from environment variables
# IMPORTANT: Replace "YOUR_GROQ_API_KEY_HERE" with your actual key or load from environment
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY", "YOUR_GROQ_API_KEY_HERE")

# --- Crew Definition --- (from MJoyBVFKrOhd and U42Sj-1sshGm)
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    verbose=True # Enable verbose output
)

# --- Crew Execution --- (from U42Sj-1sshGm)
print("\n--- Crew Execution Started ---")
# Pass inputs to kickoff to resolve the '{topic}' placeholder in research_task
result = crew.kickoff(inputs={'topic': 'AI agents'})

# --- Process and Print Output --- (from U42Sj-1sshGm and x5WHEChwrriK)
print("\n--- Generated Blog Post (Pydantic Output) ---")
blog: BlogOutput = result.pydantic # Explicitly type hint for clarity
print(f"Title: {blog.title}")
print(f"Word Count: {blog.word_count}")
print(f"Tags: {', '.join(blog.tags)}")
print("\nContent:\n", blog.content)

print("\n--- Raw Crew Output ---")
print(result.raw)

print("\n--- Individual Task Outputs ---")
for task_output in result.tasks_output:
    print(f"Description: {task_output.description}")
    print(f"Raw Output: {task_output.raw}")
    print(f"Agent: {task_output.agent.role}")

print("\n--- Token Usage ---")
print(result.token_usage)
