from pydantic import BaseModel
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from .prompt import FILE_MANAGER_PROMPT

class Result(BaseModel):
    tool_name: str
    tool_result: str


ollama_model = OpenAIModel(
    model_name='qwen3:1.7b', provider=OpenAIProvider(base_url='http://localhost:11434/v1')
)

agent = Agent(ollama_model, output_type=Result, system_prompt=FILE_MANAGER_PROMPT)


@agent.tool
def read_file(ctx: RunContext[None], filename: str) -> Result:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    return content


result = agent.run_sync("get the contents of file named : readme.md")
print(result.output)

