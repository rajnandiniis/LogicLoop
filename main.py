
import asyncio

from agents.workflow.state import State
from agents.workflow.graph import OrchestratorNode, coder

async def main():
    state = State()

    directory = "D:/Study/logic-loop/agents/developer"
    
    async with coder.iter(OrchestratorNode(f"get the list of files from -> {directory}"), state=state) as run:  
        async for node in run:  
            print('Node:', node)
          
    print('Final output:', run.result.output)


asyncio.run(main())