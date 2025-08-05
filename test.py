import requests

from pydantic import BaseModel
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

class Result(BaseModel):
    tool_name: str
    tool_result: str

class ResponseSchema(BaseModel):
    city: str
    weather_condition: str
    temperature: float


ollama_model = OpenAIModel(
    model_name='qwen3:1.7b', provider=OpenAIProvider(base_url='http://localhost:11434/v1')
)
agent = Agent(ollama_model, output_type=str)


@agent.tool
def addition(ctx: RunContext[None], a: int, b: int) -> Result:
    """adds two numbers by taking input as a and b and return their sum as results"""
    print("tool has been used")
    return a + b

api_key = "b6c50144dc714dbbb35144050252207"

@agent.tool
def get_temperature(ctx: RunContext[None], city: str) -> str:
    print("calling tool")
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)

    # 🧾 Parse the response
    if response.status_code == 200:
        data = response.json()
        location = data['location']['name']
        temp_c = data['current']['temp_c']
        condition = data['current']['condition']['text']
        result = f"📍 Location: {location}\n🌡️ Temperature: {temp_c}°C\n🌥️ Condition: {condition}"
        print("result -> ", result)
        return result
    
    else:
        error_msg = f"❌ Error: {response.status_code} - {response.text}"
        print(error_msg)
        return error_msg



# user -> query -> LLM -> checks weather he can answer it 
# yes -> no tooling
# checks appropriate tool, based the all available tools
# selects a tool -> 
#     pydantic_ai will execute the tool recommended by llm using below json format
#     output of the function exection will be returned back to LLM
# LLM using this function exection result, regenerates the NLP response
# or any other pydantic specified response.


# {
#     "tool_name" : get_temperature
#     "args" : "city"
#     "args_type" : str
#     "tool_returning" : "str"
# }

# -

@agent.tool
def get_genres(ctx:RunContext[None], genres: str) -> str:

    print(genres)
    url = "https://streaming-availability.p.rapidapi.com/genres"

    querystring = {"output_language":"en"}

    headers = {
        "x-rapidapi-key": "c77336816emsh3610a85f05a8548p113d51jsn7227ed95753d",
        "x-rapidapi-host": "streaming-availability.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

# @agent.tool
# def read_file(ctx: RunContext[None], filename: str) -> Result:
#     with open(filename, "r", encoding="utf-8") as f:
#         content = f.read()
    
#     return content
    


result = agent.run_sync("give me the contents of Readme.md file")
print(result.output)

