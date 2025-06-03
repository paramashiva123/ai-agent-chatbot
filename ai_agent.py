# Step 1: Setup API Keys
import os

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Step 2: Setup LLM & Tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

# Step 3: Setup AI Agent with Search tool functionality
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id)
    else:
        raise ValueError("Unsupported provider")

    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    agent = create_react_agent(
        model=llm,
        tools=tools
    )

    state = {
        "messages": [system_prompt] + query  # inject system prompt as first message
    }

    response = agent.invoke(state)
    messages = response.get("messages", [])

    ai_messages = [msg.content for msg in messages if isinstance(msg, AIMessage)]

    return ai_messages[-1] if ai_messages else "No response generated."
