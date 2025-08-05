import os

from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from .prompt import FILE_MANAGER_PROMPT

class Result(BaseModel):
    tool_name: str
    tool_result: str


ollama_model = OpenAIModel(
    model_name='qwen2.5:1.5b ', provider=OpenAIProvider(base_url='http://localhost:11434/v1')
)

agent = Agent(ollama_model, output_type=str, system_prompt=FILE_MANAGER_PROMPT)


@agent.tool
def get_all_files_in_codebase(ctx: RunContext[None], codebase: str) -> Result:
    """tool that can be used to retrieve list of files from a codebase directory"""
    file_list = [f for f in os.listdir(codebase) if os.path.isfile(os.path.join(codebase, f))]
    return file_list

@agent.tool
def read_file(ctx: RunContext[None], filename: str) -> Result:
    """tool that can be used to read the contents of the files"""
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    return content

@agent.tool
def write_file(ctx: RunContext[None], filename: str, content: str) -> Result:
    """tool that can be used to write the content to a files"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    directory = "D:\Study\logic-loop\agents\developer"
    result = agent.run_sync(f"get the list of files from -> {directory}")
    print(result.output)

