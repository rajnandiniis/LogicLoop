# from pydantic_ai import PydanticAgent
# from agent.tool_registry import tool_registry
# from schemas.file_schemas import FileSearchArgs, FileWriteArgs

# def execute_tool(tool_name: str, args_dict: dict):
#     tool = tool_registry.get(tool_name)
#     if not tool:
#         return {"success": False, "message": "Tool not found"}
#     fn = tool["function"]
#     args_model = eval(tool["args_schema"])
#     parsed_args = args_model(**args_dict)
#     return fn(parsed_args) if "Args" in tool["args_schema"] else fn(**args_dict)

# # Example usage:
# agent = PydanticAgent(llm="ollama/mistral", tools=tool_registry)

# def run_agent(query: str):
#     response = agent.run(query)
#     return response
from agent.tool_registry import tool_registry
from schemas.file_schemas import FileSearchArgs, FileWriteArgs, FileOperationResult
from ollama import chat  # Using Ollama's native Python binding or subprocess alternative
import json

# Helper: Tool execution with Pydantic validation
def execute_tool(tool_name: str, args_dict: dict):
    tool = tool_registry.get(tool_name)
    if not tool:
        return {"success": False, "message": f"Tool '{tool_name}' not found."}

    fn = tool["function"]
    schema_type = tool["args_schema"]

    if schema_type.endswith("Args"):
        schema_class = eval(schema_type)
        parsed_args = schema_class(**args_dict)
        return fn(parsed_args)
    else:
        return fn(**args_dict)

# Agent logic using Ollama prompt + tool selection
def run_agent(prompt: str) -> str:
    # Step 1: Ask LLM what tool to run (basic logic for now)
    system_msg = (
    "You are a file assistant. "
    "Given a user's command, return a JSON object like this:\n"
    '{"tool": "search_logs", "args": {"directory": "./logs", "extension": ".log", "keyword": "ERROR"}}\n'
    "Available tools:\n"
    "- list_files: {directory: str}\n"
    "- delete_file: {filepath: str}\n"
    "- search_logs: {directory: str, extension: str, keyword: str}\n"
    "- read_file: {filepath: str}\n"
    "- edit_file: {filepath: str, new_content: str}\n"
    "- create_file: {filepath: str, content: str}\n"
)
# The following mapping logic should be applied after tool selection and argument extraction
# Remove this block from here; see below for correct placement.


    response = chat(
        model="mistral",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": prompt}
        ]
    )

    try:
        tool_call = json.loads(response["message"]["content"])
        tool_name = tool_call["tool"]
        args = tool_call["args"]
        result = execute_tool(tool_name, args)

        if isinstance(result, FileOperationResult):
            return f"[{tool_name}] ✅ {result.message or result.data}"
        return str(result)
    except Exception as e:
        return f"❌ Failed to process: {e}"
