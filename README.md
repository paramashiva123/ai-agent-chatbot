# 🤖 LangGraph AI Agent Chatbot

This is a web-based AI chatbot application built with **FastAPI**, **Streamlit**, and **LangGraph**. The chatbot integrates multiple LLM providers (Groq, OpenAI) and optionally uses web search via **Tavily** to answer queries.

---

## 🚀 Features

- 🔄 Switch between **Groq** and **OpenAI** models
- 🌐 Optional web search using Tavily
- ✍️ Customizable system prompt for agent behavior
- 💡 Simple UI built with Streamlit
- ⚡ Backend powered by FastAPI and LangGraph's `create_react_agent`

---

## 🛠️ Project Structure

ai-agent-chatbot/
│
├── ai_agent.py # Core logic to create and invoke LangGraph agent
├── backend.py # FastAPI server for handling frontend requests
├── frontend.py # Streamlit UI for user interaction
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-agent-chatbot.git
cd ai-agent-chatbot
2. Set Up Environment
Install and activate a virtual environment using pipenv:

bash
Copy
Edit
pip install pipenv          # Install pipenv
pipenv shell                # Activate virtual environment
pipenv install langchain_openai langchain_groq langchain_community langgraph pydantic uvicorn fastapi streamlit
3. Add API Keys
Create a .env file in the root directory with the following content:

env
Copy
Edit
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
📌 You can sign up for these services and get API keys from their respective websites:

Groq

OpenAI

Tavily

💻 Running the Application
1. Start the FastAPI Backend
bash
Copy
Edit
python backend.py
This starts the API server at http://127.0.0.1:9999.

2. Start the Streamlit Frontend
Open a new terminal and run:

bash
Copy
Edit
streamlit run frontend.py
Open your browser and visit: http://localhost:8501

📬 Example Usage
Choose the LLM provider: Groq or OpenAI

Select a model:

For Groq: llama-3.3-70b-versatile, mixtral-8x7b-32768

For OpenAI: gpt-4o-mini

Enter a system prompt (optional)
Example: “Be a helpful math tutor”

Type your query

Enable web search (optional)

Click Ask Agent!
