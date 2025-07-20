# 🧠 AI File Agent with Ollama + Pydantic AI

## Features
- Local LLM execution via Ollama
- Structured tool-based reasoning with Pydantic AI
- File manipulation and searching capabilities
- CLI interface via Typer
- Secure sandboxing

## Setup

```bash
pip install -r requirements.txt
ollama run mistral
python cli/main.py ask "Search all .log files in /logs for ERROR..."
