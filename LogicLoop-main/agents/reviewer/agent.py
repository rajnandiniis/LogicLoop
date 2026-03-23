from pydantic import BaseModel, Field

from pydantic_ai import Agent
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.models.openai import OpenAIModel
from .prompt import ORCHESTRATOR_PROMPT

model = OpenAIModel(
    model_name="qwen3:1.7b", provider=OpenAIProvider(base_url='http://localhost:11434/v1')
)


class Result(BaseModel):
    next_agent: str = Field(description="name of the agent to deligate the task")


agent = Agent(model=model, output_type=Result, system_prompt=ORCHESTRATOR_PROMPT)


if __name__ == "__main__":
    result = agent.run_sync("message from developer agent")
    print(result)