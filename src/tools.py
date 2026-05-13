from crewai.tools import tool

@tool("get_news")
def get_news(topic: str) -> str:
    """Get latest news about a topic (mock for lab)"""
    return f"Latest news on {topic}: Major breakthroughs in 2025 include multi-agent frameworks, reasoning models, and on-device LLMs."
