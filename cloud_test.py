from pydantic import BaseModel
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider


class Result(BaseModel):
    tool_name: str
    result: int

# Use Cloudflare Tunnel URL
ollama_model = OpenAIModel(
    model_name='mistral:7b',
)

agent = Agent(ollama_model, output_type=Result)


@agent.tool
def addition(ctx: RunContext[None], a: int, b: int) -> Result:
    """Adds two numbers and returns their sum"""
    print("tool has been used")
    return a + b 

# Run agent
result = agent.run_sync("What is the sum of 4 and 5")
print(result.output)





import requests

# 🌤 Replace with your actual API key
