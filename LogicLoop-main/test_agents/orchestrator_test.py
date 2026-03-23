# agents/agents.py

import os
import sys

# Step 1: Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Step 2: Go one level up to reach the project root
project_root = os.path.abspath(os.path.join(current_dir, ".."))

# Step 3: Add project root to sys.path if not already present
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from agents.orchestrator.agent import agent

directory = "D:/Study/logic-loop/agents/developer"
print(agent.run_sync("get the list of files from the given directory -> {directory}"))