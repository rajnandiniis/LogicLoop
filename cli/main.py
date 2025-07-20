# import typer
# from agent.core import run_agent

# app = typer.Typer()

# @app.command()
# def ask(prompt: str):
#     result = run_agent(prompt)
#     typer.echo(result)

# if __name__ == "__main__":
#     app()
import typer
from typing import List
from agent.core import run_agent

app = typer.Typer()

@app.command()
def ask(prompt: List[str] = typer.Argument(..., help="Your instruction")):
    """
    Ask the AI agent to perform a file operation based on a natural language prompt.
    """
    full_prompt = " ".join(prompt)
    result = run_agent(full_prompt)
    typer.echo(result)

if __name__ == "__main__":
    app()
