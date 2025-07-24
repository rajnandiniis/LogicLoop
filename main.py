
import asyncio


from agents.workflow.state import State
from agents.workflow.graph import OrchestratorNode, coder

async def main():
    state = State()
    
    async with coder.iter(OrchestratorNode("checkout the content of pyproject.toml"), state=state) as run:  
        async for node in run:  
            print('Node:', node)
          
    print('Final output:', run.result.output)


asyncio.run(main())