from dataclasses import dataclass
from pydantic_ai.messages import ModelMessage

@dataclass
class State:
    orchestrator_msg: list[ModelMessage] = None
    developer_msg: list[ModelMessage] = None
    reviwer_msg: list[ModelMessage] = None
    file_manager_msg: list[ModelMessage] = None
    user_msg: list[ModelMessage] = None



