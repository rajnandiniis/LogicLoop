from pydantic import BaseModel, Field
from typing import Optional

class FileSearchArgs(BaseModel):
    directory: str
    extension: str
    keyword: str

class FileWriteArgs(BaseModel):
    filepath: str
    content: str

class FileOperationResult(BaseModel):
    success: bool
    message: Optional[str] = None
    data: Optional[str] = None
