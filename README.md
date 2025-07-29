

# 🤖 LogicLoop: A Multi-Agent AI System for Collaborative Code Generation

LogicLoop is a modular, multi-agent system designed to collaboratively generate, review, and iteratively improve code using autonomous agents and structured communication.

---

## 🚀 Key Features

- **👥 Multi-Agent Architecture**  
  Built with 5 autonomous agents:
  - **Coder Agent**: Generates initial code from user prompts
  - **Reviewer Agent**: Analyzes and critiques generated code
  - **Changes Updator Agent**: Applies reviewer feedback to revise the code
  - **Orchestrator Agent**: Manages the flow between all agents
  - **Human Feedback Agent**: Incorporates user input for guided improvement

- **🔄 Agent Graph Communication**  
  Agents interact through a custom-designed agent graph, enabling collaborative and iterative problem-solving.

- **📦 Structured Reasoning with Pydantic-AI**  
  All agent inputs and outputs are validated using **typed schemas**, ensuring consistent and structured communication.

- **🧠 Advanced Tool-Calling with Ollama**  
  Uses Ollama-hosted models (e.g., Mistral, Deepseek) to perform LLM-driven reasoning and task execution.  

- **🌐 Cloudflared API Deployment**  
  LLM endpoints are exposed securely via **Cloudflared tunnels**, compatible with OpenAI-style APIs.

- **🔁 Human-in-the-Loop Feedback**  
  Integrates user feedback loops for dynamic re-prompting and improvement.

- **🧱 Modular & Extensible**  
  Easily plug in new agents or tools for complex workflows or task expansion.

---

## 📂 Project Structure

```

logicloop/
├── agents/
│   ├── coder\_agent.py
│   ├── reviewer\_agent.py
│   ├── updater\_agent.py
│   ├── orchestrator\_agent.py
│   └── human\_feedback\_agent.py
├── schemas/
│   └── io\_models.py          # Pydantic schemas for agent communication
├── tools/
│   └── ollama\_interface.py   # Tool calling wrappers
├── server/
│   └── api\_server.py         # Cloudflared OpenAI-compatible endpoint
├── main.py                   # Entry point for orchestrating agents
└── README.md

````

---

## 🛠️ Requirements

- Python 3.10+
- [LangChain](https://github.com/langchain-ai/langchain)
- [Ollama](https://ollama.ai/)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [Cloudflared](https://developers.cloudflare.com/cloudflared/)
- Other dependencies: See `requirements.txt` (coming soon)

---

## 🧪 Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/irajnandiniis/LogicLoop.git
cd LogicLoop

# 2. Start Ollama locally
ollama run mistral

# 3. Run the orchestrator
python main.py
````

---

## 🧠 Example Use Case

1. User gives a prompt:
   *"Write a Python script to scrape headlines from Hacker News."*

2. The system generates initial code → reviews → applies feedback → allows user corrections → returns final code.

---

## 🔐 Secure API via Cloudflared (Optional)

Expose the orchestrator as an OpenAI-compatible endpoint:

```bash
cloudflared tunnel --url http://localhost:8000
```

Use this URL in any OpenAI-compatible client.

---

## 🙋‍♀️ Contributing

Feel free to open issues or PRs. The system is modular and welcomes new agent ideas, tools, or LLM integrations.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Rajnandini** – [@rajnandiniis](https://github.com/irajnandiniis)

```

---

Let me know if you want:
- A `requirements.txt`
- A diagram of agent flow
- A Streamlit UI or LangGraph integration reference

Ready to paste and go!
```
