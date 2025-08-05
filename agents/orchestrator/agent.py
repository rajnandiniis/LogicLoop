from pydantic import BaseModel, Field
from typing import Literal
from pydantic_ai import Agent
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.models.openai import OpenAIModel
from agents.orchestrator.prompt import ORCHESTRATOR_PROMPT

model = OpenAIModel(
    model_name="qwen3:1.7b", provider=OpenAIProvider(base_url='http://localhost:11434/v1')
)

class Result(BaseModel):
    """format for the response of the orchestrator agent"""
    next_agent: Literal["file_manager", "user", "developer", "reviewer"]

class Failure(BaseModel):
    reason: str = Field("reason of the failure of task")

agent = Agent(
    model=model,
    output_type=Result | Failure,
    system_prompt=ORCHESTRATOR_PROMPT,
)

if __name__ == "__main__":
    try:
        result = agent.run_sync("message from developer agent")
        print(result)
    except Exception as e:
        print("Agent failed to produce valid output:", e)