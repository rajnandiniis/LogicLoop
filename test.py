from pydantic import BaseModel

from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider


class Result(BaseModel):
    tool_name: str
    result: int

ollama_model = OpenAIModel(
    model_name='mistral:7b', provider=OpenAIProvider(base_url='http://localhost:11434/v1')
)
agent = Agent(ollama_model, output_type=Result)


@agent.tool
def addition(ctx: RunContext[None], a: int, b: int) -> Result:
    """adds two numbers by taking input as a and b and return their sum as results"""
    print("tool has been used")
    return a + b


result = agent.run_sync("What is the sum of 4 and 5")
print(result.output)
