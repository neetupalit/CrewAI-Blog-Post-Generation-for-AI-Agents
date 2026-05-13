# CrewAI Blog Post Generation

This project demonstrates how to set up and use the `crewai` library to generate blog posts on various topics. It features a research agent and a writing agent working collaboratively to produce structured, informative content.

## Project Structure

- `README.md`: This file.
- `requirements.txt`: Lists all Python dependencies.
- `notebooks/crewai_blog_post_generation.ipynb`: The Google Colab notebook containing the interactive development steps.
- `src/`: Contains the modularized Python code for agents, tasks, tools, and the crew orchestration.
  - `__init__.py`: Makes `src` a Python package.
  - `tools.py`: Defines the custom tool used by agents.
  - `agents.py`: Defines the `researcher` and `writer` agents.
  - `tasks.py`: Defines the `research_task` and `write_task`, including Pydantic output modeling.
  - `crew_runner.py`: Orchestrates the agents and tasks into a `Crew` and executes the workflow.

## Features

*   **Agents:** Two specialized agents (`researcher` and `writer`) with distinct roles, goals, and backstories.
    *   `researcher`: Focuses on finding accurate information about a given topic.
    *   `writer`: Creates clear, engaging blog posts based on the research findings.
*   **Tasks:** Well-defined tasks for each agent, with clear descriptions and expected outputs, supporting dynamic input (`{topic}`).
*   **Crew Orchestration:** Uses `crewai.Crew` to manage the workflow, with sequential processing.
*   **Pydantic Output:** Leverages Pydantic models to ensure the final blog post output is structured and validated (title, content, word count, tags).
*   **Custom Tool:** Includes a mock `get_news` tool to simulate external data fetching.

## Setup and Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/crewai-blog-generation.git
    cd crewai-blog-generation
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set your GROQ_API_KEY:**
    Obtain an API key from [Groq Cloud](https://console.groq.com/). Set it as an environment variable:
    ```bash
    export GROQ_API_KEY="your-groq-api-key"
    ```
    If running in Google Colab, you can use `os.environ["GROQ_API_KEY"] = "your-groq-api-key"` or the Colab Secrets Manager.

## How to Run

### Via Python Script

To run the crew and generate a blog post from the command line:

```bash
python src/crew_runner.py
```

This will execute the defined agents and tasks, producing a blog post about 'AI agents' as specified in `crew_runner.py`.

### Via Google Colab Notebook

Open `notebooks/crewai_blog_post_generation.ipynb` in Google Colab. Ensure your `GROQ_API_KEY` is set in the appropriate cell (e.g., `uWeo8PLup0pj`) and run all cells sequentially.

## Key Fixes and Learnings During Development

This project involved resolving several common `crewai` and Python development challenges:

1.  **`SyntaxError: invalid syntax` for YAML-like configurations:** Initial agent and task definitions were in a YAML-like format. These were refactored into valid Python dictionaries and `crewai.Task` object instantiations.
2.  **`NameError: name 'agent_name' is not defined`:** Agents were not properly instantiated as `crewai.Agent` objects before being referenced in tasks. This was corrected by instantiating them using configuration dictionaries and specifying an LLM.
3.  **`AttributeError: 'function' object has no attribute 'kickoff'`:** A variable named `crew` was inadvertently overwritten by a function definition (due to a `@crew` decorator from a `CrewBase` class). The `crew` variable was re-instantiated as a `crewai.Crew` object directly before calling `kickoff()`.
4.  **Missing `inputs` for `crew.kickoff()`:** Tasks with dynamic placeholders (e.g., `{topic}`) require an `inputs` dictionary to be passed to the `crew.kickoff()` method to fill these placeholders at runtime.
