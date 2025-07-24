from __future__ import annotations
from dataclasses import dataclass

from pydantic_graph import BaseNode, End, Graph, GraphRunContext
from .state import State
from agents.orchestrator.agent import agent as orchestrator_agent
from agents.file_manager.agent import agent as file_manager_agent


@dataclass
class OrchestratorNode(BaseNode[State]):
    orchestrator_msg: str

    async def run(self, ctx:GraphRunContext[State]) -> FileManagerNode | End:
        response = await orchestrator_agent.run(self.orchestrator_msg)
        ctx.state.orchestrator_msg += response.new_messages()

        if response.output.next_agent == "file_manager":
            return FileManagerNode(response.new_messages())
        
        return End

        
@dataclass
class FileManagerNode(BaseNode[State]):
    file_manager_msg: str

    async def run(self, ctx: GraphRunContext[State]) -> OrchestratorNode:
        response = await file_manager_agent.run(self.file_manager_msg)
        ctx.state.file_manager_msg += response.new_messages()
        return OrchestratorNode(response.new_messages())
    


coder = Graph(
    nodes=[OrchestratorNode, FileManagerNode]
)
