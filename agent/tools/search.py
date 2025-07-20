import os
from schemas.file_schemas import FileSearchArgs, FileOperationResult

def search_logs(args: FileSearchArgs) -> FileOperationResult:
    result_lines = []
    try:
        for filename in os.listdir(args.directory):
            if filename.endswith(args.extension):
                with open(os.path.join(args.directory, filename), 'r') as f:
                    for line in f:
                        if args.keyword in line:
                            result_lines.append(line.strip())
        return FileOperationResult(success=True, data='\n'.join(result_lines))
    except Exception as e:
        return FileOperationResult(success=False, message=str(e))
