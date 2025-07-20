from agent.tools import file_ops, search

tool_registry = {
    "list_files": {
        "function": file_ops.list_files,
        "description": "List files in a directory.",
        "args_schema": "directory:str"
    },
    "delete_file": {
        "function": file_ops.delete_file,
        "description": "Delete a specific file.",
        "args_schema": "filepath:str"
    },
    "search_logs": {
    "function": search.search_logs,
    "description": "Search for a keyword in log files.",
    "args_schema": "FileSearchArgs"
    },
    "read_file": {
    "function": file_ops.read_file,
    "description": "Read the contents of a file.",
    "args_schema": "filepath:str"
},
"edit_file": {
    "function": file_ops.edit_file,
    "description": "Append content to a file.",
    "args_schema": "filepath:str, new_content:str"
},
"create_file": {
    "function": file_ops.create_file,
    "description": "Create a new file with content.",
    "args_schema": "filepath:str, content:str"
},


}
