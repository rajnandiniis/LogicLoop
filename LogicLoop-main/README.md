# 🤖 LogicLoop: Multi-Agent AI System for Collaborative Code Generation

> What if AI didn’t just generate code — but **thought, reviewed, and improved it like a team of engineers?**

**LogicLoop** is an experimental multi-agent AI system where multiple agents collaborate to generate, review, and refine code through structured workflows and feedback loops.

---

## 🌟 Why This Project Exists

Most AI coding tools work like this:

👉 Prompt → Output → Done  

But real software development is **iterative**:

- Write code  
- Review it  
- Fix issues  
- Improve based on feedback  

**LogicLoop simulates this real-world workflow using AI agents.**

---

## 🚀 What Makes It Interesting

### 👥 Multi-Agent Collaboration

Instead of one model, LogicLoop uses **5 specialized agents**:

- **Coder Agent** → Generates initial code  
- **Reviewer Agent** → Finds issues and suggests improvements  
- **Updater Agent** → Applies fixes based on feedback  
- **Orchestrator Agent** → Controls the workflow  
- **Human Feedback Agent** → Adds real user input  

👉 This creates a loop similar to a real dev team.

---

### 🔄 Iterative Improvement Loop

The system doesn’t stop at first output.

It continuously:

1. Generates code  
2. Reviews it  
3. Improves it  
4. Accepts human feedback  
5. Refines again  

---

### 🧠 Structured AI Communication

- Uses **Pydantic schemas** to enforce structured inputs/outputs  
- Reduces randomness in LLM responses  
- Makes agent communication more reliable  

---

### 🛠️ Tool-Driven Reasoning

- Integrated with **Ollama (local LLMs like Mistral, DeepSeek)**  
- Supports tool calling for controlled execution  
- Designed for experimentation with different models  

---

### 🔐 Local-First & Secure

- Runs with **locally hosted models (via Ollama)**  
- No dependency on external APIs  
- Better for privacy and cost control  

---

## 🌍 Real-World Relevance

LogicLoop reflects how modern AI systems are evolving:

- Multi-agent systems (AutoGPT-style workflows)  
- Human-in-the-loop AI  
- Iterative reasoning instead of one-shot outputs  

👉 Useful for:
- AI-assisted coding tools  
- Automated code review systems  
- Developer productivity tools  
- Research in agent-based AI systems  

---

## 🧩 System Flow

```mermaid
graph TD
    A[User Prompt] --> B[Coder Agent]
    B --> C[Reviewer Agent]
    C --> D[Updater Agent]
    D --> E[Orchestrator]
    E --> F[Human Feedback]
    F --> B
````

---

## 📂 Project Structure

```
logicloop/
├── agents/
│   ├── coder_agent.py
│   ├── reviewer_agent.py
│   ├── updater_agent.py
│   ├── orchestrator_agent.py
│   └── human_feedback_agent.py
├── schemas/
│   └── io_models.py
├── tools/
│   └── ollama_interface.py
├── server/
│   └── api_server.py
├── main.py
└── README.md
```

---

## 🛠️ Tech Stack

* Python
* Pydantic
* Ollama (Mistral, DeepSeek)
* LangChain (optional integration)
* Cloudflared (for API exposure)

---

## ⚙️ Getting Started

### 1. Clone Repository

```bash
git clone https://github.com/irajnandiniis/LogicLoop.git
cd LogicLoop
```

### 2. Start Ollama

```bash
ollama run mistral
```

### 3. Run the System

```bash
python main.py
```

---

## 🧠 Example

**Input:**

> Write a Python script to scrape headlines from Hacker News

**What happens internally:**

* Code is generated
* Reviewed for issues
* Improved automatically
* User feedback is applied
* Final version is produced

---

## 🔐 Optional: API Exposure

```bash
cloudflared tunnel --url http://localhost:8000
```

Use this as an OpenAI-compatible endpoint.

---

## 🧠 What I Learned

* Multi-agent systems are more effective than single LLM calls
* Structured communication reduces hallucinations
* Feedback loops significantly improve output quality
* Real AI systems require orchestration, not just models

---

## 🤝 Contributing

Contributions are welcome:

1. Fork the repo
2. Create a branch
3. Add features / agents
4. Submit a PR

---

## ⭐ Final Thought

AI is moving from **single responses → collaborative systems**

LogicLoop is a small step in exploring that direction.


