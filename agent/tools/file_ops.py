import os
from schemas.file_schemas import FileOperationResult

def list_files(directory: str) -> FileOperationResult:
    try:
        files = os.listdir(directory)
        return FileOperationResult(success=True, data='\n'.join(files))
    except Exception as e:
        return FileOperationResult(success=False, message=str(e))

def delete_file(filepath: str) -> FileOperationResult:
    try:
        os.remove(filepath)
        return FileOperationResult(success=True, message="File deleted.")
    except Exception as e:
        return FileOperationResult(success=False, message=str(e))
def read_file(filepath: str) -> FileOperationResult:
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        return FileOperationResult(success=True, data=content)
    except Exception as e:
        return FileOperationResult(success=False, message=str(e))

def edit_file(filepath: str, new_content: str) -> FileOperationResult:
    try:
        with open(filepath, 'a') as f:  # append mode
            f.write('\n' + new_content)
        return FileOperationResult(success=True, message="Content added successfully.")
    except Exception as e:
        return FileOperationResult(success=False, message=str(e))
def create_file(filepath: str, content: str) -> FileOperationResult:
    try:
        with open(filepath, 'w') as f:
            f.write(content)
        return FileOperationResult(success=True, message="File created.")
    except Exception as e:
        return FileOperationResult(success=False, message=str(e))
