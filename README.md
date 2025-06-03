# 🤖 LangGraph AI Agent Chatbot

This is a web-based AI chatbot application built with **FastAPI**, **Streamlit**, and **LangGraph**. The chatbot integrates multiple LLM providers (Groq, OpenAI) and optionally uses web search via **Tavily** to answer queries.

---

## 🚀 Features

- 🔄 Switch between **Groq** and **OpenAI** models
- 🌐 Optional web search using Tavily
- ✍️ Customizable system prompt for agent behavior
- 💡 Simple UI using Streamlit
- ⚡ Backend built with FastAPI and LangGraph's `create_react_agent`

---

## 🛠️ Project Structure

ai-agent-chatbot/
│
├── ai_agent.py # Core logic to create and invoke LangGraph agent
├── backend.py # FastAPI server for handling frontend requests
├── frontend.py # Streamlit UI for user interaction
├── requirements.txt # Python dependencies
└── README.md # You're here!

yaml
Copy
Edit

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-agent-chatbot.git
cd ai-agent-chatbot
2. Set up environment
Create and activate a virtual environment:

bash
Copy
Edit
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Add API keys
Create a .env file in the root directory:

env
Copy
Edit
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
You can sign up for these services and get API keys from their respective websites:

Groq

OpenAI

Tavily

💻 Running the Application
1. Start the FastAPI backend
bash
Copy
Edit
python backend.py
This starts the API server at http://127.0.0.1:9999.

2. Start the Streamlit frontend
In a new terminal:

bash
Copy
Edit
streamlit run frontend.py
Open your browser at: http://localhost:8501

📬 Example Usage
Choose the LLM provider: Groq or OpenAI

Select the model (e.g., llama-3.3-70b-versatile or gpt-4o-mini)

Type your system prompt (optional, e.g., "Be a helpful math tutor")

Enter your query

Enable web search if needed

Click Ask Agent!

🧪 Sample Prompt
text
Copy
Edit
System Prompt: You are a professional financial advisor.
User Query: What are good investment options for beginners in 2025?
