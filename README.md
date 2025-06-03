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
├── ai_agent.py        # Core logic to create and invoke LangGraph agent
├── backend.py         # FastAPI server for handling frontend requests
├── frontend.py        # Streamlit UI for user interaction
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```


### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-agent-chatbot.git
cd ai-agent-chatbot
<<<<<<< HEAD
```

### 2. Set Up Environment

Install and activate a virtual environment using `pipenv`:

```bash
pip install pipenv          # Install pipenv
pipenv shell                # Activate virtual environment
pipenv install langchain_openai langchain_groq langchain_community langgraph pydantic uvicorn fastapi streamlit
```

### 3. Add API Keys

Create a `.env` file in the root directory with the following content:

```env
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

> 📌 You can sign up for these services and get API keys from their respective websites:
> - [Groq](https://console.groq.com/)
> - [OpenAI](https://platform.openai.com/)
> - [Tavily](https://www.tavily.com/)

---

## 💻 Running the Application

### 1. Start the FastAPI Backend

```bash
python backend.py
```

This starts the API server at `http://127.0.0.1:9999`.

### 2. Start the Streamlit Frontend

Open a **new terminal** and run:

```bash
streamlit run frontend.py
```

Open your browser and visit: [http://localhost:8501](http://localhost:8501)

---

## 📬 Example Usage

1. Choose the **LLM provider**: `Groq` or `OpenAI`
2. Select a **model**:  
   - For Groq: `llama-3.3-70b-versatile`, `mixtral-8x7b-32768`  
   - For OpenAI: `gpt-4o-mini`
3. Enter a **system prompt** (optional)  
   _Example_: “Be a helpful math tutor”
4. Type your **query**
5. Enable **web search** (optional)
6. Click **Ask Agent!**

---

## 🧪 Sample Prompt

```text
System Prompt: You are a professional financial advisor.
User Query: What are good investment options for beginners in 2025?
```

## 🙌 Acknowledgements

- [LangGraph by LangChain](https://www.langchain.com/langgraph)
- [Streamlit](https://streamlit.io)
- [FastAPI](https://fastapi.tiangolo.com)
- [Tavily Search](https://www.tavily.com)
=======
